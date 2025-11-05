from typing import Any, Callable, TypeVar, Generic
T = TypeVar("T")

class MyProperty(Generic[T]):
    def __init__(self, getter: Callable[[Any], T]) -> None:
        self.getter = getter

    def __get__(self, obj, objtype=None) -> T:
        return self.getter(obj)

class Person:
    def __init__(self) -> None:
        self.x = 7400.5

    @MyProperty
    def salary(self) -> float:
        return self.x

