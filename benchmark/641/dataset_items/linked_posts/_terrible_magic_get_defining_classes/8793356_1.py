>>> C.foo.im_func
<function foo at 0x1062dfaa0>
>>> inspect.isfunction(C.foo.im_func)
True
>>> inspect.ismethod(C.foo.im_func)
False
