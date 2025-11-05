def sq_shortest_dist_to_point(self, other_point):
    dx = self.b.x - self.a.x
    dy = self.b.y - self.a.y
    dr2 = float(dx ** 2 + dy ** 2)

    lerp = ((other_point.x - self.a.x) * dx + (other_point.y - self.a.y) * dy) / dr2
    if lerp < 0:
        lerp = 0
    elif lerp > 1:
        lerp = 1

    x = lerp * dx + self.a.x
    y = lerp * dy + self.a.y

    _dx = x - other_point.x
    _dy = y - other_point.y
    square_dist = _dx ** 2 + _dy ** 2
    return square_dist

def shortest_dist_to_point(self, other_point):
    return math.sqrt(self.sq_shortest_dist_to_point(other_point))
