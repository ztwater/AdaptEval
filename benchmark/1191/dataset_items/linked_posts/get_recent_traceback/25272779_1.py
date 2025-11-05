try:
    a = 1/0
except Exception as e:
    lines = traceback.format_exc().splitlines()
    print (lines)
