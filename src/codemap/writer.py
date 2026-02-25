from datetime import datetime


def build_markdown(tree_text: str, root_path, plugin_name: str) -> str:
    header = (
        "# CodeMap\n\n"
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Root: {root_path}\n"
        f"Framework: {plugin_name}\n\n"
        "```\n"
    )

    footer = "\n```\n"

    return header + tree_text + footer


def write_file(output_path, content: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)