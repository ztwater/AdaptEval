def trace_caller():
    try:
        raise Exception
    except Exception:
        frame = sys.exc_info()[2].tb_frame.f_back.f_back
        print(" >> invoked by:", frame.f_code.co_name)
