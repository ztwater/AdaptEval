import numpy as np
from matplotlib import path, transforms

def clip_boxes(box0, box1):
    path_coords = np.array([[box0[0, 0], box0[0, 1]],
                            [box0[1, 0], box0[0, 1]],
                            [box0[1, 0], box0[1, 1]],
                            [box0[0, 0], box0[1, 1]]])

    poly = path.Path(np.vstack((path_coords[:, 0],
                                path_coords[:, 1])).T, closed=True)
    clip_rect = transforms.Bbox(box1)

    poly_clipped = poly.clip_to_bbox(clip_rect).to_polygons()[0]

    return np.array([np.min(poly_clipped, axis=0),
                     np.max(poly_clipped, axis=0)])

box0 = np.array([[0, 0], [1, 1]])
box1 = np.array([[0, 0], [0.5, 0.5]])

print clip_boxes(box0, box1)
