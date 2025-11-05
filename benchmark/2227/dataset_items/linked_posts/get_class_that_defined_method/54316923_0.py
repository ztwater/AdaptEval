>>> class particular_purpose: 
...     def __init__(self, fn): 
...         self.fn = fn 
...      
...     def __set_name__(self, owner, name): 
...         owner._particular_purpose.add(self.fn) 
...          
...         # then replace ourself with the original method 
...         setattr(owner, name, self.fn) 
...  
... class A: 
...     _particular_purpose = set() 
...  
...     @particular_purpose 
...     def hello(self): 
...         return "hello" 
...  
...     @particular_purpose 
...     def world(self): 
...         return "world" 
...  
>>> A._particular_purpose
{<function __main__.A.hello(self)>, <function __main__.A.world(self)>}
>>> a = A() 
>>> for fn in A._particular_purpose: 
...     print(fn(a)) 
...                                                                                                                                     
world
hello
