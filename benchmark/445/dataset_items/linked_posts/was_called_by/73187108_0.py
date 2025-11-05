def method1():
    method2()

def method2():
    try:
        raise Exception
    except Exception:
        frame = sys.exc_info()[2].tb_frame.f_back

    print("method2 invoked by: ", frame.f_code.co_name)

# Invoking method1
method1()
