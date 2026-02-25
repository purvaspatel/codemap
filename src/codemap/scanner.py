from pathlib import Path
from .constants import GLOBAL_IGNORE, GLOBAL_HIDDEN_FILES


def build_tree(path: Path, plugin):
    name = path.name

    if path.is_file():
        return {
            "type": "file",
            "name": name,
        }

    children = []

    for item in sorted(path.iterdir(), key=lambda x: x.name.lower()):
        if item.name in GLOBAL_IGNORE:
            continue

        if plugin and item.name in plugin.ignore:
            continue

        if item.name in GLOBAL_HIDDEN_FILES:
            continue

        if plugin and item.name in plugin.hidden_files:
            continue
            
        if item.name.endswith(".egg-info"):
            continue

        if item.is_dir() and plugin and item.name in plugin.collapse:
            children.append({
                "type": "dir",
                "name": item.name,
                "collapsed": True,
            })
            continue

        children.append(build_tree(item, plugin))

        if item.name == "codemap.md":
            continue

    return {
        "type": "dir",
        "name": name,
        "children": children,
    }