frames = inspect.stack()

className = None
for frame in frames[1:]:
    if frame[3] == "<module>":
        # At module level, go no further
        break
    elif '__module__' in frame[0].f_code.co_names:
        className = frame[0].f_code.co_name
        break
