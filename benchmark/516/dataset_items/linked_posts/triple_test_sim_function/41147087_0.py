from pathlib import Path
path = Path('/my/directory/filename.txt')
path.parent.mkdir(parents=True, exist_ok=True) 
# path.parent ~ os.path.dirname(path)
