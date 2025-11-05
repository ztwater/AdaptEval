from pathlib import Path

p = Path('/home/my/path')
sorted(list(p.glob('**/*.png')))
