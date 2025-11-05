def get_iou(var_0, var_1):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.

    Parameters
    ----------
    bb1 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x1, y1) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner
    bb2 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x, y) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner

    Returns
    -------
    float
        in [0, 1]
    """
    assert var_0['x1'] < var_0['x2']
    assert var_0['y1'] < var_0['y2']
    assert var_1['x1'] < var_1['x2']
    assert var_1['y1'] < var_1['y2']

    # determine the coordinates of the intersection rectangle
    var_2 = max(var_0['x1'], var_1['x1'])
    var_3 = max(var_0['y1'], var_1['y1'])
    var_4 = min(var_0['x2'], var_1['x2'])
    var_5 = min(var_0['y2'], var_1['y2'])

    if var_4 < var_2 or var_5 < var_3:
        return 0.0

    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box
    var_6 = (var_4 - var_2) * (var_5 - var_3)

    # compute the area of both AABBs
    var_7 = (var_0['x2'] - var_0['x1']) * (var_0['y2'] - var_0['y1'])
    var_8 = (var_1['x2'] - var_1['x1']) * (var_1['y2'] - var_1['y1'])

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    var_9 = var_6 / float(var_7 + var_8 - var_6)
    assert var_9 >= 0.0
    assert var_9 <= 1.0
    return var_9
