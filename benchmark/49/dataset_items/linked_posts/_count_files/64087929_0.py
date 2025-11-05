import os 

def count_files_in_dir(path: str) -> int:
    file_entries = [entry for entry in os.scandir(path) if entry.is_file()]

    return len(file_entries)
