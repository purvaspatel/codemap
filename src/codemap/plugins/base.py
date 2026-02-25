class BasePlugin:
    name = "base"

    # Files that indicate the current framework
    detection_files = []

    # Files to ignore when scanning the code
    ignore = set()

    # Show folder but do not traverse inside
    collapse = set()

    # Files that should never be shown
    hidden_files = set()

    def matches(self, root_path):
        from pathlib import Path

        for file in self.detection_files:
            if (Path(root_path) / file).exists():
                return True
        return False

