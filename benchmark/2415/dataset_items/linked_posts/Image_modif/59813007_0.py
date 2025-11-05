import cv2
import numpy as np

def saturate(img, percentile):
    """Changes the scale of the image so that half of percentile at the low range
    becomes 0, half of percentile at the top range becomes 255.
    """

    if 2 != len(img.shape):
        raise ValueError("Expected an image with only one channel")

    # copy values
    channel = img[:, :].copy()
    flat = channel.ravel()

    # copy values and sort them
    sorted_values = np.sort(flat)

    # find points to clip
    max_index = len(sorted_values) - 1
    half_percent = percentile / 200
    low_value = sorted_values[math.floor(max_index * half_percent)]
    high_value = sorted_values[math.ceil(max_index * (1 - half_percent))]

    # saturate
    channel[channel < low_value] = low_value
    channel[channel > high_value] = high_value

    # scale the channel
    channel_norm = channel.copy()
    cv2.normalize(channel, channel_norm, 0, 255, cv2.NORM_MINMAX)

    return channel_norm

def adjust_gamma(img, gamma):
    """Build a lookup table mapping the pixel values [0, 255] to
    their adjusted gamma values.
    """

    # code from
    # https://www.pyimagesearch.com/2015/10/05/opencv-gamma-correction/

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

    # apply gamma correction using the lookup table
    return cv2.LUT(img, table)


def adjust_brightness_with_gamma(gray_img, minimum_brightness, gamma_step = GAMMA_STEP):

    """Adjusts the brightness of an image by saturating the bottom and top
    percentiles, and changing the gamma until reaching the required brightness.
    """
    if 3 <= len(gray_img.shape):
        raise ValueError("Expected a grayscale image, color channels found")

    cols, rows = gray_img.shape
    changed = False
    old_brightness = np.sum(gray_img) / (255 * cols * rows)
    new_img = gray_img
    gamma = 1

    while True:
        brightness = np.sum(new_img) / (255 * cols * rows)
        if brightness >= minimum_brightness:
            break

        gamma += gamma_step
        new_img = adjust_gamma(gray_img, gamma = gamma)
        changed = True

    if changed:
        print("Old brightness: %3.3f, new brightness: %3.3f " %(old_brightness, brightness))
    else:
        print("Maintaining brightness at %3.3f" % old_brightness)

    return new_img

def main(filepath):

    img = cv2.imread(filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    saturated = saturate(gray, 1)
    bright = adjust_brightness_with_gamma(saturated, minimum_brightness = 0.66)
