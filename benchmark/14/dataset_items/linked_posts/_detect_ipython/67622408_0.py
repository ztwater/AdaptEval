import traceback

def is_in_notebook():
    rstk = traceback.extract_stack(limit=1)[0]
    return rstk[0].startswith("<ipython")
