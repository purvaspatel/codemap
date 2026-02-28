import subprocess
import typer
from pathlib import Path
from .root import find_project_root, detect_plugin
from .scanner import build_tree
from .formatter import format_tree
from .writer import build_markdown, write_file

app = typer.Typer(invoke_without_command=True)


@app.callback()
def main():
    start_path = Path.cwd()

    root = find_project_root(start_path)

    if not root:
        typer.secho(
            "Error: No project root detected.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=1)

    if root != start_path:
        typer.secho(
            f"Detected project root at: {root}",
            fg=typer.colors.CYAN,
        )

    plugin = detect_plugin(root)

    output_file = root / "codemap.md"

    # Build tree
    tree = build_tree(root, plugin)
    tree_text = format_tree(tree)

    # Build full markdown content
    new_content = build_markdown(
        tree_text,
        root,
        plugin.name if plugin else "unknown",
    )

    if output_file.exists():
        old_content = output_file.read_text(encoding="utf-8")

        # Extract old tree block
        if "```" in old_content:
            old_tree = old_content.split("```")[1].strip()
        else:
            old_tree = ""

        if old_tree == tree_text.strip():
            typer.secho(
                "No structural changes detected. codemap.md is up to date.",
                fg=typer.colors.BLUE,
            )
        else:
            # Structure changed → rewrite file with new timestamp
            write_file(output_file, new_content)

            typer.secho(
                "codemap.md updated successfully.",
                fg=typer.colors.YELLOW,
            )
    else:
        write_file(output_file, new_content)

        typer.secho(
            "codemap.md generated successfully.",
            fg=typer.colors.GREEN,
        )

    typer.echo()
    typer.echo(tree_text)

    try:
        subprocess.run("pbcopy", input=tree_text.encode(), check=True)
        typer.secho("Tree copied to clipboard.", fg=typer.colors.GREEN)
    except FileNotFoundError:
        try:
            subprocess.run(
                ["xclip", "-selection", "clipboard"],
                input=tree_text.encode(),
                check=True,
            )
            typer.secho("Tree copied to clipboard.", fg=typer.colors.GREEN)
        except FileNotFoundError:
            pass