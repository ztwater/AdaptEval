-- if the (poly-)line has several segments, just iterate through all of them:
function nearest_sector_in_line (x, y, line)
    local x1, y1, x2, y2, min_dist
    local ax,ay = line[1], line[2]
    for j = 3, #line-1, 2 do
        local bx,by = line[j], line[j+1]
        local dist = distPointToLine(x,y,ax,ay,bx,by)
        if not min_dist or dist < min_dist then
            min_dist = dist
            x1, y1, x2, y2 = ax,ay,bx,by
        end
        ax, ay = bx, by
    end
    return x1, y1, x2, y2
end
