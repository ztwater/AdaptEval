z_masked = np.multiply(z,mask)

zimg_masked = plt.imshow(z_masked,cmap="gray")
plt.show()
