import inspect
frame = inspect.stack()[-1]
print(frame.filename)
