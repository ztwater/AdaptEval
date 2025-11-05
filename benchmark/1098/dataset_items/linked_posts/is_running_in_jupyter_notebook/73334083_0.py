import psutil
def runninginJupyterNotebook():
    for i in psutil.Process().parent().cmdline():
        if "jupyter-notebook" in i:
            return True
    else:
        return False
