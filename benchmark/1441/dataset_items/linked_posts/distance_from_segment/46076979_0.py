var a = { x:20, y:20};//start segment    
var b = { x:40, y:30};//end segment   
var c = { x:37, y:14};//point   

// magnitude from a to c    
var ac = Math.sqrt( Math.pow( ( a.x - c.x ), 2 ) + Math.pow( ( a.y - c.y ), 2) );    
// magnitude from b to c   
var bc = Math.sqrt( Math.pow( ( b.x - c.x ), 2 ) + Math.pow( ( b.y - c.y ), 2 ) );    
// magnitude from a to b (base)     
var ab = Math.sqrt( Math.pow( ( a.x - b.x ), 2 ) + Math.pow( ( a.y - b.y ), 2 ) );    
 // perimeter of triangle     
var p = ac + bc + ab;    
 // area of the triangle    
var area = Math.sqrt( p/2 * ( p/2 - ac) * ( p/2 - bc ) * ( p/2 - ab ) );    
 // height of the triangle = distance    
var h = ( area * 2 ) / ab;    
console.log ("height: " + h);
