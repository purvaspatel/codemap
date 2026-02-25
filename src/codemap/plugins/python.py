from .base import BasePlugin

class PythonPlugin(BasePlugin):
    name = "python"

    detection_files = ["pyproject.toml","requirements.txt","setup.py"]

    ignore = {
        "__pycache__",
        ".venv",
        "venv",
        "env",
        ".env",
        ".mypy_cache",
        ".pytest_cache",
    }

    collapse = set()

    hidden_files = {
        ".env",
        ".env.local",
    }