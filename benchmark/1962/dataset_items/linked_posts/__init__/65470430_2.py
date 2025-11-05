$ python t.py
Traceback (most recent call last):
  File "t.py", line 26, in <module>
    class C:
  File "t.py", line 20, in dec
    class D(cls):
  File "/usr/lib/python3.8/functools.py", line 57, in update_wrapper
    getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
AttributeError: 'mappingproxy' object has no attribute 'update'
