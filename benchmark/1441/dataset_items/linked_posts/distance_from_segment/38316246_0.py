function solveLinearEquation(A1,B1,C1,A2,B2,C2)
--it is the implitaion of a method of solving linear equations in x and y
  local f1 = B1*C2 -B2*C1
  local f2 = A2*C1-A1*C2
  local f3 = A1*B2 -A2*B1
  return {x= f1/f3, y= f2/f3}
end


function pointLiesOnLine(x,y,x1,y1,x2,y2)
  local dx1 = x-x1
  local  dy1 = y-y1
  local dx2 = x-x2
  local  dy2 = y-y2
  local crossProduct = dy1*dx2 -dx1*dy2

if crossProduct ~= 0  then  return  false
else
  if ((x1>=x) and (x>=x2)) or ((x2>=x) and (x>=x1)) then
    if ((y1>=y) and (y>=y2)) or ((y2>=y) and (y>=y1)) then
      return true
    else return false end
  else  return false end
end
end


function dist(x1,y1,x2,y2)
  local dx = x1-x2
  local dy = y1-y2
  return math.sqrt(dx*dx + dy* dy)
 end


function findMinDistBetnPointAndLine(x1,y1,x2,y2,x3,y3)
-- finds the min  distance between (x3,y3) and line (x1,y2)--(x2,y2)
   local A2,B2,C2,A1,B1,C1
   local dx = y2-y1
   local dy = x2-x1
   if dx == 0 then A2=1 B2=0 C2=-x3 A1=0 B1=1 C1=-y1 
   elseif dy == 0 then A2=0 B2=1 C2=-y3 A1=1 B1=0 C1=-x1
   else
      local m1 = dy/dx
      local m2 = -1/m1
      A2=m2 B2=-1 C2=y3-m2*x3 A1=m1 B1=-1 C1=y1-m1*x1
   end
 local intsecPoint= solveLinearEquation(A1,B1,C1,A2,B2,C2)
if pointLiesOnLine(intsecPoint.x, intsecPoint.y,x1,y1,x2,y2) then
   return dist(intsecPoint.x, intsecPoint.y, x3,y3)
 else
   return math.min(dist(x3,y3,x1,y1),dist(x3,y3,x2,y2))
end
end
