import numpy as np

def polygon_area(coords):
    # get x and y in vectors
    x = [point[0] for point in coords]
    y = [point[1] for point in coords]
    # shift coordinates
    x_ = x - np.mean(x)
    y_ = y - np.mean(y)
    # calculate area
    correction = x_[-1] * y_[0] - y_[-1] * x_[0]
    main_area = np.dot(x_[:-1], y_[1:]) - np.dot(y_[:-1], x_[1:])
    return 0.5 * np.abs(main_area + correction)

#### Example output
coords = [(385495.19520441635, 6466826.196947694), (385496.1951836388, 6466826.196947694), (385496.1951836388, 6466825.196929455), (385495.19520441635, 6466825.196929455), (385495.19520441635, 6466826.196947694)]

Shapely's area method:  0.9999974610685296
@Trenton's area method: 0.9999974610685296
