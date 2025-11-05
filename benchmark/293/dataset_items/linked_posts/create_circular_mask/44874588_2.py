h, w = img.shape[:2]
mask = create_circular_mask(h, w)
masked_img = img.copy()
masked_img[~mask] = 0
