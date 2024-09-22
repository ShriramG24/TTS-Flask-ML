import os


def extract_text_from_file(file_path: str) -> str:
    if file_path is None or not file_path.endswith(".txt"):
        return None
    try:
        with open(file_path, "r") as f:
            return f.read()
    except (FileNotFoundError, UnicodeDecodeError):
        return None


def extract_file_name(file_path: str) -> str:
    file_name, _ = os.path.splitext(os.path.basename(file_path))
    return file_name


def extract_text_files_from_dir(directory: str) -> list[str]:
    if directory is None or not os.path.isdir(directory):
        return None

    text_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                filepath = os.path.join(root, file)
                text_files.append(filepath)

    return text_files if len(text_files) > 0 else None
