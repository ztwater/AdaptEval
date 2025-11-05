surface = np.zeros([1024,1024])
surface[1:1+10, 1:1+10] += 1
surface[100:100+500, 100:100+100] += 1
unionArea = (surface==2).sum()
print(unionArea)
