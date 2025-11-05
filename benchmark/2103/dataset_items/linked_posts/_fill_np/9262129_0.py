from scipy import ndimage as nd

indices = nd.distance_transform_edt(invalid_cell_mask, return_distances=False, return_indices=True)
data = data[tuple(ind)]
