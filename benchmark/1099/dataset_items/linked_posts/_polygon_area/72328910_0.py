def find_int_coordinates(n: int, coords: list[list[int]]) -> float:
    rez = 0
    x, y = coords[n - 1]
    for coord in coords:
        rez += (x + coord[0]) * (y - coord[1])
        x, y = coord
    return abs(rez / 2)
