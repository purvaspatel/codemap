from .base import BasePlugin


class JavaScriptPlugin(BasePlugin):
    name = "javascript"

    detection_files = ["package.json"]

    ignore = {
        ".next",
        "dist",
        "build",
    }

    collapse = {
        "node_modules",
    }

    hidden_files = {
        ".env",
        ".env.local",
    }