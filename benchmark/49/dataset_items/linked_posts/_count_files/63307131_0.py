from pathlib import Path

path = Path('.')

print(sum(1 for _ in path.glob('*')))  # Files and folders, not recursive
print(sum(1 for _ in path.rglob('*')))  # Files and folders, recursive

print(sum(1 for x in path.glob('*') if x.is_file()))  # Only files, not recursive
print(sum(1 for x in path.rglob('*') if x.is_file()))  # Only files, recursive
