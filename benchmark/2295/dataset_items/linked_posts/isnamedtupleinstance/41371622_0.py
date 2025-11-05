from collections import namedtuple

SomeThing = namedtuple('SomeThing', 'prop another_prop')
SomeOtherThing = namedtuple('SomeOtherThing', 'prop still_another_prop')

a = SomeThing(1, 2)

isinstance(a, SomeThing) # True
isinstance(a, SomeOtherThing) # False
