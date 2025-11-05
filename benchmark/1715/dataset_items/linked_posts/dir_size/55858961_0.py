from pathlib import Path

sum([f.stat().st_size for f in Path("path").glob("**/*")])
