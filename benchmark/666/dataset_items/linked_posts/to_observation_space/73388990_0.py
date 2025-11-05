@dataclass
class Point:
   x: int
   y: int

p = Point(10, 20)
asdict(p) # it returns {'x': 10, 'y': 20}
