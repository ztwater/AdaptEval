def print_bmatrix(matrix, precision=0):
    matrix = matrix.tolist()
    print('\\begin{bmatrix}')
    for row in matrix[:-1]:
        print_row(row,precision)
    print_last_row(matrix[-1],precision)
    print('\\end{bmatrix}')

def print_row(row,precision):
    for item in row[:-1]:
        print(format(item,'.'+str(precision)+'f'), end=' & ')
    print(format(row[-1],'.'+str(precision)+'f')+'\\\\')

def print_last_row(row,precision):
    for item in row[:-1]:
        print(format(item,'.'+str(precision)+'f'), end=' & ')
    print(format(row[-1],'.'+str(precision)+'f')) 
