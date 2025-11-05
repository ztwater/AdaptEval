__init__.py

$ diff __init__.py Original
64c64
< def load(stream, Loader=Loader, **kwds):
---
> def load(stream, Loader=Loader):
69c69
<     loader = Loader(stream, **kwds)
---
>     loader = Loader(stream)
75c75
< def load_all(stream, Loader=Loader, **kwds):
---
> def load_all(stream, Loader=Loader):
80c80
<     loader = Loader(stream, **kwds)
---
>     loader = Loader(stream)

constructor.py

$ diff constructor.py Original
20,21c20
<     def __init__(self, object_pairs_hook=dict):
<         self.object_pairs_hook = object_pairs_hook
---
>     def __init__(self):
27,29d25
<     def create_object_hook(self):
<         return self.object_pairs_hook()
<
54,55c50,51
<         self.constructed_objects = self.create_object_hook()
<         self.recursive_objects = self.create_object_hook()
---
>         self.constructed_objects = {}
>         self.recursive_objects = {}
129c125
<         mapping = self.create_object_hook()
---
>         mapping = {}
400c396
<         data = self.create_object_hook()
---
>         data = {}
595c591
<             dictitems = self.create_object_hook()
---
>             dictitems = {}
602c598
<             dictitems = value.get('dictitems', self.create_object_hook())
---
>             dictitems = value.get('dictitems', {})

loader.py

$ diff loader.py Original
13c13
<     def __init__(self, stream, **constructKwds):
---
>     def __init__(self, stream):
18c18
<         BaseConstructor.__init__(self, **constructKwds)
---
>         BaseConstructor.__init__(self)
23c23
<     def __init__(self, stream, **constructKwds):
---
>     def __init__(self, stream):
28c28
<         SafeConstructor.__init__(self, **constructKwds)
---
>         SafeConstructor.__init__(self)
33c33
<     def __init__(self, stream, **constructKwds):
---
>     def __init__(self, stream):
38c38
<         Constructor.__init__(self, **constructKwds)
---
>         Constructor.__init__(self)
