#Define grid of N*N
N = 4
rng = np.random.default_rng(10)

pos =  np.array(np.meshgrid(np.linspace(0,1,N),np.linspace(0,1,N), indexing = 'ij')).T
vec_black = rng.uniform(-1, 1, (N*N, 2))
vec_grey = rng.uniform(-1, 1, (N*N, 2))
theta_black_grey = angle(vec_black, vec_grey, axis=-1)

import matplotlib.pyplot as plt
width = 0.008
scale = 8
plt.figure()
plt.quiver(*pos.T, *vec_black.T, color = 'k', width = width, scale = scale)
plt.quiver(*pos.T, *vec_grey.T, color = 'grey', width = width, scale = scale)
plt.scatter(*pos.T, c=theta_black_grey,  cmap ='hsv', vmin=-np.pi, vmax = np.pi)
plt.xlim([-0.3,1.3])
plt.ylim([-0.3,1.3])
plt.colorbar(label='Angle (black arrow, grey arrow)')
