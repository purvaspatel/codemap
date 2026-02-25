def format_tree(tree):
    lines = [tree["name"]]

    def _format(node, prefix=""):
        children = node.get("children", [])
        total = len(children)

        for index, child in enumerate(children):
            connector = "└── " if index == total - 1 else "├── "
            line = prefix + connector + child["name"]
            lines.append(line)

            if child["type"] == "dir" and not child.get("collapsed"):
                extension = "    " if index == total - 1 else "│   "
                _format(child, prefix + extension)

    _format(tree)
    return "\n".join(lines)