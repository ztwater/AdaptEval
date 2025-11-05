def row_col_from_condensed_index(d,index):
    b = 1 - (2 * d) 
    i = (-b - math.sqrt(b ** 2 - 8 * index)) // 2
    j = index + i * (b + i + 2) // 2 + 1
    return (i,j)  
