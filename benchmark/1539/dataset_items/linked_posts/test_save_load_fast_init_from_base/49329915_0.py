from copy import deepcopy
from typing import TypeVar

Cls = TypeVar('Cls')


# This type hint is a dirty lie to make autocomplete and static
# analyzers give more useful results. Crazy the stuff you can do
# with python...
def copy_class(cls: Cls) -> Cls:
    copy_cls = type(f'{cls.__name__}Copy', cls.__bases__, dict(cls.__dict__))
    for name, attr in cls.__dict__.items():
        try:
            hash(attr)
        except TypeError:
            # Assume lack of __hash__ implies mutability. This is NOT
            # a bullet proof assumption but good in many cases.
            setattr(copy_cls, name, deepcopy(attr))
    return copy_cls


def test_copy_class():
    class A(object):
        mutable_class_var = []

    ACopy = copy_class(A)

    a = A()
    acopy = ACopy()

    acopy.mutable_class_var.append(1)
    assert a.mutable_class_var == []
    assert A.mutable_class_var == []
    assert ACopy.mutable_class_var == [1]
    assert acopy.mutable_class_var == [1]
