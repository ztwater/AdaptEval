def zip_dir(filename: str, dir_to_zip: pathlib.Path):
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Use glob instead of iterdir(), to cover all subdirectories.
        for directory in dir_to_zip.glob('**'):
            for file in directory.iterdir():
                if not file.is_file():
                    continue
                # Strip the first component, so we don't create an uneeded subdirectory
                # containing everything.
                zip_path = pathlib.Path(*file.parts[1:])
                # Use a string, since zipfile doesn't support pathlib  directly.
                zipf.write(str(file), str(zip_path))
