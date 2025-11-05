RUNNING_IN_JUPYTER = any([i.endswith("bin/jupyter-notebook") for i in psutil.Process().parent().cmdline()])
