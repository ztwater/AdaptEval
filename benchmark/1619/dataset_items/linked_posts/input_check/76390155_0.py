from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid


fig = plt.figure()
plot = ImageGrid(fig, 111, (1, 1),
                 cbar_mode='single',
                 cbar_location='right',
                 cbar_size='3%',
                 cbar_pad='5%')
im = plot[0].imshow(np.random.randn(2**4, 2**6))
cbar = fig.colorbar(im, cax=plot.cbar_axes[0])
