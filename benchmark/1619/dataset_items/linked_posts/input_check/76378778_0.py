data = [(1,2,3,4,5),(4,5,6,7,8),(7,8,9,10,11)]

im = plt.imshow(data, cmap='RdBu')
l, b, w, h = plt.gca().get_position().bounds
cax = plt.gcf().add_axes([l + w + 0.03, b, 0.03, h])
plt.colorbar(im, cax=cax)
