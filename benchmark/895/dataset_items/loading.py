import numpy as np

class LoadBuildingAnnotations:
    """Load multiple types of annotations.

    Args:
        with_bbox (bool): Whether to parse and load the bbox annotation.
             Default: True.
        with_label (bool): Whether to parse and load the label annotation.
            Default: True.
        with_mask (bool): Whether to parse and load the mask annotation.
             Default: False.
        with_seg (bool): Whether to parse and load the semantic segmentation
            annotation. Default: False.
        poly2mask (bool): Whether to convert the instance masks from polygons
            to bitmaps. Default: True.
        denorm_bbox (bool): Whether to convert bbox from relative value to
            absolute value. Only used in OpenImage Dataset.
            Default: False.
        file_client_args (dict): Arguments to instantiate a FileClient.
            See :class:`mmcv.fileio.FileClient` for details.
            Defaults to ``dict(backend='disk')``.
    """

    def __init__(
        self,
        with_bbox=True,
        with_label=True,
        with_mask=False,
        with_seg=False,
        poly2mask=True,
        denorm_bbox=False,
        key_points=False,
        key_points_weight=1,
        num_points=0,
        spline_num=10,
        training=True,
        file_client_args=dict(backend="disk"),
    ):
        self.with_bbox = with_bbox
        self.with_label = with_label
        self.with_mask = with_mask
        self.with_seg = with_seg
        self.poly2mask = poly2mask
        self.denorm_bbox = denorm_bbox
        self.file_client_args = file_client_args.copy()
        self.file_client = None
        self.num_points = num_points
        self.spline_num = spline_num
        self.spline_poly_num = num_points * 10
        self.key_points = key_points
        self.key_points_weight = key_points_weight
        self.training = training


    def _polygon_area(self, poly):
        """Compute the area of a component of a polygon.

        Using the shoelace formula:
        https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates

        Args:
            x (ndarray): x coordinates of the component
            y (ndarray): y coordinates of the component

        Return:
            float: the are of the component
        """
        x = poly[:, 0]
        y = poly[:, 1]
        return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
