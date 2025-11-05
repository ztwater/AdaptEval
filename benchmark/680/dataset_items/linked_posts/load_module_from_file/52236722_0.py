import pathlib

def likely_python_module(filename):
    '''
    Given a filename or Path, return the "likely" python module name.  That is, iterate
    the parent directories until it doesn't contain an __init__.py file.

    :rtype: str
    '''
    p = pathlib.Path(filename).resolve()
    paths = []
    if p.name != '__init__.py':
        paths.append(p.stem)
    while True:
        p = p.parent
        if not p:
            break
        if not p.is_dir():
            break

        inits = [f for f in p.iterdir() if f.name == '__init__.py']
        if not inits:
            break

        paths.append(p.stem)

    return '.'.join(reversed(paths))
