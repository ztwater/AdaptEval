RUNNING_IN_JUPYTER = any(["jupyter-notebook" in i for i in psutil.Process().parent().cmdline()])
