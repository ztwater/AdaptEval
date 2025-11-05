@enforce_types
@dataclasses.dataclass
class Point:
    x: float
    y: float

@enforce_types
def foo(bar: typing.Union[int, str]):
    pass
