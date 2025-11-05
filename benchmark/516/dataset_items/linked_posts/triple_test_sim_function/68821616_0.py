from pathlib import Path

path_to_file = Path("zero/or/more/directories/file.ext")
parent_directory_of_file = path_to_file.parent
parent_directory_of_file.mkdir(parents=True, exist_ok=True)
