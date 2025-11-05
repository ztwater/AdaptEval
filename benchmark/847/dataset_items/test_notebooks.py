from pathlib import Path

def convert_notebook_to_py(nb_fn: Path, py_fn: Path) -> None:
    """
    From https://stackoverflow.com/questions/17077494/how-do-i-convert-a-ipython-notebook-into-a-python-file-via-commandline
    """
    import nbformat
    from nbconvert import PythonExporter

    with open(nb_fn) as fh:
        nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)

    exporter = PythonExporter()
    source, meta = exporter.from_notebook_node(nb)
    # Skip the magic, which gets converted to `get_ipython()`
    source = source.replace("get_ipython", "# get_ipython")

    with open(py_fn, "w+") as fh:
        # fh.writelines(source.encode('utf-8'))
        fh.writelines(source)
