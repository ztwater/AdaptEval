kernel = gaussian_heatmap(center = (2, 2), image_size = (10, 10), sig = 1)
plt.imshow(kernel)
print("max at :", np.unravel_index(kernel.argmax(), kernel.shape))
print("kernel shape", kernel.shape)
