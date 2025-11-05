def count_number_of_raw_data_point_files(path: Union[str, Path], with_file_prefix: str) -> int:
    import os
    path: Path = force_expanduser(path)

    _, _, files = next(os.walk(path))
    # file_count = len(files)
    filename: str
    count: int = 0
    for filename in files:
        print(f'-->{filename=}')  # e.g. print -->filename='data_point_99.json'
        if with_file_prefix in filename:
            count += 1
    return count
