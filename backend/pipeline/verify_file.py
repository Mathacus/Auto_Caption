from pathlib import Path

def check_path(file):
    file_path = Path(file)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.touch(exist_ok=True)