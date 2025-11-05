sum(file.stat().st_size for file in Path(folder).rglob('*'))
