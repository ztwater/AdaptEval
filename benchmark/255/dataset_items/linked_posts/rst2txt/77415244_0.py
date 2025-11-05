import subprocess


def rst_to_plain_text(rst_file: Union[str, Path], tmpfile="tmp.txt") -> str:
    """use linux command 'more' to read contents of a reStructuredText format file to string

    Args:
        rst_file (Union[str, Path]): filepath to .rst file
        tmpfile (str, optional): temporary file to write as plain text

    Returns:
        str: plain text version of rst file
    """
    subprocess.check_output(f"more {rst_file} > {tmpfile}", shell=True)
    with open(tmpfile, "r") as f:
        txt = f.read()
    return txt

