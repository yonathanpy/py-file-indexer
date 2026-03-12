import os


def parse_file(path):

    try:

        with open(path, "r", encoding="utf-8", errors="ignore") as f:

            content = f.read()

        return {
            "path": path,
            "name": os.path.basename(path),
            "content": content
        }

    except Exception:

        return None
