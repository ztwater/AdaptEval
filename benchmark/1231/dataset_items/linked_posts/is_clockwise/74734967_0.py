let polygon = [
  {x:5,y:0},
  {x:6,y:4},
  {x:4,y:5},
  {x:1,y:5},
  {x:1,y:0}
]
document.body.innerHTML += `Polygon ${polygon.map(p=>`(${p.x}, ${p.y})`).join(", ")} is clockwise? ${isPolygonClockwise(polygon)}`

let reversePolygon = []
polygon.forEach(point=>reversePolygon.unshift(point))
document.body.innerHTML += `<br/>Polygon ${reversePolygon.map(p=>`(${p.x}, ${p.y})`).join(", ")} is clockwise? ${isPolygonClockwise(reversePolygon)}`

function isPolygonClockwise (polygon) {
  // From http://www.faqs.org/faqs/graphics/algorithms-faq/ "How do I find the orientation of a simple polygon?"
  // THIS SOMETIMES FAILS if the polygon is a figure 8, or similar shape where it crosses over itself
  
  // Take the lowest point (break ties with the right-most). 
  if (polygon.length < 3) {
    return true // A single point or two points can't be clockwise/counterclockwise
  }
  let previousPoint = polygon[0]
  let lowestPoint = polygon[1]
  let nextPoint = polygon[2]
  polygon.forEach((point, index)=>{
    if (point.y > lowestPoint.y || (point.y === lowestPoint.y && point.x > lowestPoint.x)) { // larger y values are lower, in svgs
      // Break ties with furthest right
      previousPoint = polygon[(index-1) >= (0)                ? (index-1) : (polygon.length-1)]
      lowestPoint = polygon[index]
      nextPoint = polygon[(index+1)     <= (polygon.length-1) ? (index+1) : (0)]
    }
  })
  // Check the angle between the previous point, that point, and the next point.
  // If the angle is less than PI radians, the polygon is clockwise
  let angle = findAngle(previousPoint, lowestPoint, nextPoint)
  return angle < Math.PI
}

function findAngle(A,B,C) {
  var AB = Math.atan2(B.y-A.y, B.x-A.x);
  var BC = Math.atan2(C.y-B.y, C.x-B.x);
  if (AB < 0) AB += Math.PI*2
  if (BC < 0) BC += Math.PI*2
  return BC-AB;
}