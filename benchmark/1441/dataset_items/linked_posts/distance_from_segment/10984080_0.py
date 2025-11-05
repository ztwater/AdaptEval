for p1, p2 in vertices:

  var r = dotProduct(vector(p2 - p1), vector(x - p1))
  //x is the point you're looking for

  r /= (magnitude(vector(p2 - p1)) ** 2)

  if r < 0:
    var dist = magnitude(vector(x - p1))
  else if r > 1:
    dist = magnitude(vector(p2 - x))
  else:
    dist = sqrt(magnitude(vector(x - p1)) ^ 2 - (r * magnitude(vector(p2-p1))) ^ 2)

  minDist = min(dist,minDist)
