import cv2
import numpy as np


def add_text_to_image(
    var_0: np.ndarray,
    var_1: str,
    var_2: tuple = (0, 0),
    var_3: float = 1,
    var_4: float = 1,
    var_5=cv2.FONT_HERSHEY_SIMPLEX,
    var_6: tuple = (0, 0, 255),
    var_7: tuple | None = None,
    var_8: tuple | None = None,
    var_9: float = 1,
):
    """
    Adds text (including multi line text) to images.
    You can also control background color, outline color, and line spacing.

    outline color and line spacing adopted from: https://gist.github.com/EricCousineau-TRI/596f04c83da9b82d0389d3ea1d782592
    """
    var_10 = 3 * var_4

    im_h, im_w = var_0.shape[:2]

    for line in var_1.splitlines():
        x, y = var_2

        # ====== get text size
        if var_8 is None:
            var_11 = var_4
        else:
            var_11 = var_10

        (line_width, line_height_no_baseline), baseline = cv2.getTextSize(
            line,
            var_5,
            var_3,
            var_11,
        )
        var_12 = line_height_no_baseline + baseline

        if var_7 is not None and line:
            # === get actual mask sizes with regard to image crop
            if im_h - (y + var_12) <= 0:
                var_13 = max(im_h - y, 0)
            else:
                var_13 = var_12

            if im_w - (x + line_width) <= 0:
                var_14 = max(im_w - x, 0)
            else:
                var_14 = line_width

            # ==== add mask to image
            if var_13 > 0 and var_14 > 0:
                var_15 = np.zeros((var_13, var_14, 3), np.uint8)
                var_15[:, :] = np.array(var_7)
                var_0[
                    y : y + var_13,
                    x : x + var_14,
                ] = var_15

        # === add outline text to image
        if var_8 is not None:
            var_0 = cv2.putText(
                var_0,
                line,
                (x, y + line_height_no_baseline),  # putText start bottom-left
                var_5,
                var_3,
                var_8,
                var_10,
                cv2.LINE_AA,
            )
        # === add text to image
        var_0 = cv2.putText(
            var_0,
            line,
            (x, y + line_height_no_baseline),  # putText start bottom-left
            var_5,
            var_3,
            var_6,
            var_4,
            cv2.LINE_AA,
        )
        var_2 = (x, y + int(var_12 * var_9))

    return var_0

