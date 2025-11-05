# Length along line that is closest to the point
print(line.project(p))

# Now combine with interpolated point on line
p2 = line.interpolate(line.project(p))
print(p2)  # POINT (5 7)
