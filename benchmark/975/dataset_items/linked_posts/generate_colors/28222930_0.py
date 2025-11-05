from itertools import cycle
cycol = cycle('bgrcmk')

for X,Y in data:
    scatter(X, Y, c=cycol.next())
