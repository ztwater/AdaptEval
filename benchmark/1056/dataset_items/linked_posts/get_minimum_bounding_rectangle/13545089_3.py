# add after pi = ... line:
minRect = (1e33, 0, 0, 0, 0, 0, 0) # area, dx, dy, i, iL, iP, iR

# add after area = ... line:
    if area < minRect[0]:
        minRect = (area, xR-xL, yP-yC, i, iL, iP, iR)

# add after print ... line:
print 'Min rectangle:', minRect
# or instead of that print, add:
print 'Min rectangle: ',
for x in ['{:3d} '.format(x) if isinstance(x, int) else '{:7.3f} '.format(x) for x in minRect]:
    print x,
print
