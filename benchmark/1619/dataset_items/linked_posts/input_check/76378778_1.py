import matplotlib.pyplot as plt

def add_colorbar(im, width=None, pad=None, **kwargs):

    l, b, w, h = im.axes.get_position().bounds       # get boundaries
    width = width or 0.1 * w                         # get width of the colorbar
    pad = pad or width                               # get pad between im and cbar
    fig = im.axes.figure                             # get figure of image
    cax = fig.add_axes([l + w + pad, b, width, h])   # define cbar Axes
    return fig.colorbar(im, cax=cax, **kwargs)       # draw cbar
    

data = [(1,2,3,4,5),(4,5,6,7,8),(7,8,9,10,11)]

# an example usage
im = plt.imshow(data, cmap='RdBu')
add_colorbar(im)
