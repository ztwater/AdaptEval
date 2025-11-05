>>> class A:
...     def a(self): pass
... 
>>> class B:
...     def b(self): pass
... 
>>> class C(A, B):
...     def a(self): pass
... 
>>> A.a
<function A.a at 0x7f13b58dfc80>
>>> get_class_that_defined_method(A.a)
this is a function
<class '__main__.A'>
>>>
>>> A().a
<bound method A.a of <__main__.A object at 0x7f13b58ca9e8>>
>>> get_class_that_defined_method(A().a)
this is a method
<class '__main__.A'>
>>>
>>> C.a
<function C.a at 0x7f13b58dfea0>
>>> get_class_that_defined_method(C.a)
this is a function
<class '__main__.C'>
>>>
>>> C().a
<bound method C.a of <__main__.C object at 0x7f13b58ca9e8>>
>>> get_class_that_defined_method(C().a)
this is a method
<class '__main__.C'>
>>>
>>> C.b
<function B.b at 0x7f13b58dfe18>
>>> get_class_that_defined_method(C.b)
this is a function
<class '__main__.B'>
>>>
>>> C().b
<bound method C.b of <__main__.C object at 0x7f13b58ca9e8>>
>>> get_class_that_defined_method(C().b)
this is a method
<class '__main__.B'>
