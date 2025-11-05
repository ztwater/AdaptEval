import numpy as np

# Create 10 random floats in range 0..1 in array "b"
b = np.random.random_sample((10,)).astype(np.float32)

# Save to file
np.save('BunchOfFloats.npy',b)

# Read back into different array "r"
r = np.load('BunchOfFloats.npy')

# Inspect b 
array([0.26565347, 0.7193414 , 0.19435954, 0.58980538, 0.28096624,
   0.88655137, 0.84847042, 0.80156026, 0.94315194, 0.76888901])

# Inspect r
array([0.26565347, 0.7193414 , 0.19435954, 0.58980538, 0.28096624,
   0.88655137, 0.84847042, 0.80156026, 0.94315194, 0.76888901])
