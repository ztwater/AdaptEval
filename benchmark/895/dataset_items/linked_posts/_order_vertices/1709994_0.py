L = [
  { "lat": 34.495239, "lng": -118.127747 }, # north-west
  { "lat": 34.495239, "lng": -117.147217 }, # north-east
  { "lat": 34.095174, "lng": -117.147217 }, # south-east
  { "lat": 34.095174, "lng": -118.127747 }  # south-west
]


L = sorted(L, key=lambda k: (-k["lat"], -k["lng"]))

L[-2], L[-1] = L[-1], L[-2]
import pprint
pprint.pprint(L)
