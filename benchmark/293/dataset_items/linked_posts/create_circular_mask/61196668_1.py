z = image.imread('robot.jpg')  
z = z[:,:,1]

zimg = plt.imshow(z,cmap="gray")
plt.show()
