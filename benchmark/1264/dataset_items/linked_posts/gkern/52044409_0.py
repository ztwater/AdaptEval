def get_gauss_kernel(size=3,sigma=1):
    center=(int)(size/2)
    kernel=np.zeros((size,size))
    for i in range(size):
       for j in range(size):
          diff_sq = (i-center)**2+(j-center)**2
          kernel[i,j]=np.exp(-diff_sq/(2*sigma**2))
    return kernel/np.sum(kernel)
