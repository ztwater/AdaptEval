from pathlib import Path

def get_size(folder: str) -> int:
    return sum(p.stat().st_size for p in Path(folder).rglob('*'))
