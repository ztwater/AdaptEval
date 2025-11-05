-- distance from point (px, py) to line segment (x1, y1, x2, y2)
function distPointToLine(px,py,x1,y1,x2,y2) -- point, start and end of the segment
    local dx,dy = x2-x1,y2-y1
    local length = math.sqrt(dx*dx+dy*dy)
    dx,dy = dx/length,dy/length -- normalization
    local p = dx*(px-x1)+dy*(py-y1)
    if p < 0 then
        dx,dy = px-x1,py-y1
        return math.sqrt(dx*dx+dy*dy), x1, y1 -- distance, nearest point
    elseif p > length then
        dx,dy = px-x2,py-y2
        return math.sqrt(dx*dx+dy*dy), x2, y2 -- distance, nearest point
    end
    return math.abs(dy*(px-x1)-dx*(py-y1)), x1+dx*p, y1+dy*p -- distance, nearest point
end
