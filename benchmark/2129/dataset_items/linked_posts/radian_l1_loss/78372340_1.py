for i = 360, -360, -180 do
    for j = -120, 120, 120 do
        local a1 = math.rad (i)
        local a2 = math.rad (j)
        local dy1, dx1 = math.sin (a1), math.cos (a1)
        local dy2, dx2 = math.sin (a2), math.cos (a2)
        local dif = angleComparing(dx1, dy1, dx2, dy2)
        print (i, j, string.format('%.1f', math.deg (dif)))
    end
end
