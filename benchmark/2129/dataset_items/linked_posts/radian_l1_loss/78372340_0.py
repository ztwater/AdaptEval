function angleComparing(x1, y1, x2, y2)
    local a1 = math.atan2(y1, x1)
    local a2 = math.atan2(y2, x2)
    local diff = (a2 - a1 + math.pi)%(2*math.pi) - math.pi
    return diff -- returns values in range [-pi, pi]
end
