import matplotlib.pyplot as plt
for n in range(10):
    points = np.random.rand(4,2)
    plt.scatter(points[:,0], points[:,1])
    bbox = minimum_bounding_rectangle(points)
    plt.fill(bbox[:,0], bbox[:,1], alpha=0.2)
    plt.axis('equal')
    plt.show()
