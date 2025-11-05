>>> def x(self): pass
... 
>>> class Z:
...     y = x
...     z = (lambda: lambda: 1)()  # this returns the inner function
...     @classmethod
...     def class_meth(cls): pass
...     @staticmethod
...     def static_meth(): pass
...
>>> x
<function x at 0x7f13b58dfa60>
>>> get_class_that_defined_method(x)
this is a function
<function x at 0x7f13b58dfa60>
>>>
>>> Z.y
<function x at 0x7f13b58dfa60>
>>> get_class_that_defined_method(Z.y)
this is a function
<function x at 0x7f13b58dfa60>
>>>
>>> Z().y
<bound method Z.x of <__main__.Z object at 0x7f13b58ca9e8>>
>>> get_class_that_defined_method(Z().y)
this is a method
this is neither a function nor a method
>>>
>>> Z.z
<function Z.<lambda>.<locals>.<lambda> at 0x7f13b58d40d0>
>>> get_class_that_defined_method(Z.z)
this is a function
<class '__main__.Z'>
>>>
>>> Z().z
<bound method Z.<lambda> of <__main__.Z object at 0x7f13b58ca9e8>>
>>> get_class_that_defined_method(Z().z)
this is a method
this is neither a function nor a method
>>>
>>> Z.class_meth
<bound method type.class_meth of <class '__main__.Z'>>
>>> get_class_that_defined_method(Z.class_meth)
this is a method
this is neither a function nor a method
>>>
>>> Z().class_meth
<bound method type.class_meth of <class '__main__.Z'>>
>>> get_class_that_defined_method(Z().class_meth)
this is a method
this is neither a function nor a method
>>>
>>> Z.static_meth
<function Z.static_meth at 0x7f13b58d4158>
>>> get_class_that_defined_method(Z.static_meth)
this is a function
<class '__main__.Z'>
>>>
>>> Z().static_meth
<function Z.static_meth at 0x7f13b58d4158>
>>> get_class_that_defined_method(Z().static_meth)
this is a function
<class '__main__.Z'>
