kernel = gaussian_heatmap(center = (25, 40), image_size = (100, 50), sig = 5)
plt.imshow(kernel)
print("max at :", np.unravel_index(kernel.argmax(), kernel.shape))
print("kernel shape", kernel.shape)
