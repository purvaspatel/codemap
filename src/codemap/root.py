from pathlib import Path
from typing import Optional
from .plugins.python import PythonPlugin
from .plugins.javascript import JavaScriptPlugin

PLUGINS = [
    PythonPlugin(),
    JavaScriptPlugin(),
]

def find_project_root(start_path: Path) -> Optional[Path]:
    current = start_path.resolve()

    while current != current.parent:
        for plugin in PLUGINS:
            for marker in plugin.detection_files:
                if (current / marker).exists():
                    return current
        if (current / ".git").exists():
            return current
        current = current.parent

    return None


def detect_plugin(root_path: Path):
    for plugin in PLUGINS:
        if plugin.matches(root_path):
            return plugin
    return None