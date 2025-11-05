from pathlib import Path

[f.unlink() for f in Path("/path/to/folder").glob("*") if f.is_file()] 
