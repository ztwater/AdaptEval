frame = inspect.currentframe()
while frame:
    if has_what_i_want(frame):  # customize
        return what_i_want(frame)  # customize
    frame = frame.f_back
