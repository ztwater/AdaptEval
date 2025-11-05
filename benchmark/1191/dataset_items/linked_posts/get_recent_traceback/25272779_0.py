try:
    # something which throws
except Exception as expt:
    import traceback
    trace_lines = traceback.format.exc().splitlines()
    # tracelines contains all the lines from the traceback
    # Accordingly filter for e.g. check for lines containing File and then extract only the filename from the complete path and print it
