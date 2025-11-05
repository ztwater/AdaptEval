def vec_row_col(d,i):                                                                
    i = np.array(i)                                                                 
    b = 1 - 2 * d                                                                   
    x = np.floor((-b - np.sqrt(b**2 - 8*i))/2).astype(int)                                      
    y = (i + x*(b + x + 2)/2 + 1).astype(int)                                                    
    if i.shape:                                                                     
        return zip(x,y)                                                             
    else:                                                                           
        return (x,y) 
