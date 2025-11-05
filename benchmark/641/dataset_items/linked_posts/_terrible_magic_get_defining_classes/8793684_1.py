import inspect
frames = inspect.stack()
defined_in_class = False
if len(frames) > 2:
    maybe_class_frame = frames[2]
    statement_list = maybe_class_frame[4]
    first_statment = statement_list[0]
    if first_statment.strip().startswith('class '):
        defined_in_class = True
