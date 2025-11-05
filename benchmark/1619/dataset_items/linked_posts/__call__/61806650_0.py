# Image size
M, N = 1000, 1000

# Generate synthetic image
image = np.tile(np.arange(0,N,dtype='float64'),(M,1)) * 20

# -- sqrt(mu) * normal(0,1) --
poisson_noise = np.sqrt(image) * np.random.normal(0, 1, image.shape)

# Add the noise to the mu values
noisy_image = image + poisson_noise

plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.title('Image')
plt.imshow(image,'gray')
plt.subplot(2,2,2)
plt.title('Noisy image noise')
plt.imshow(noisy_image,'gray')  
plt.subplot(2,2,3)
plt.title('Image profile')
plt.plot(image[0,:])
plt.subplot(2,2,4)
plt.title('Noisy image profile')
plt.plot(noisy_image[0,:])

print("Synthetic image mean: {}".format(image[:,1].mean()))
print("Synthetic image variance: {}".format(image[:,1].var()))    
print("Noisy image mean: {}".format(noisy_image[:,1].mean()))
print("Noisy image variance: {}".format(noisy_image[:,1].var()))
