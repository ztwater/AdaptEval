def calc_iou(roi1, roi2):
    # Sum all "white" pixels clipped to 1
    U = np.sum(np.clip(roi1 + roi2, 0 , 1))
    # +1 for each overlapping white pixel (these will = 2)
    I = len(np.where(roi1 + roi2 == 2)[0])
    return(I/U)
