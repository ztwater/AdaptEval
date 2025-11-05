PERCENTILE_STEP = 1
GAMMA_STEP = 0.01

def adjust_brightness_alpha_beta_gamma(gray_img, minimum_brightness, percentile_step = PERCENTILE_STEP, gamma_step = GAMMA_STEP):
    """Adjusts brightness with histogram clipping by trial and error.
    """

    if 3 <= len(gray_img.shape):
        raise ValueError("Expected a grayscale image, color channels found")

    new_img = gray_img
    percentile = percentile_step
    gamma = 1
    brightness_changed = False

    while True:
        cols, rows = new_img.shape
        brightness = np.sum(new_img) / (255 * cols * rows)

        if not brightness_changed:
            old_brightness = brightness

        if brightness >= minimum_brightness:
            break

        # adjust alpha and beta
        percentile += percentile_step
        alpha, beta = percentile_to_bias_and_gain(new_img, percentile)
        new_img = convertScale(gray_img, alpha = alpha, beta = beta)
        brightness_changed = True

        # adjust gamma
        gamma += gamma_step
        new_img = adjust_gamma(new_img, gamma = gamma)

    if brightness_changed:
        print("Old brightness: %3.3f, new brightness: %3.3f " %(old_brightness, brightness))
    else:
        print("Maintaining brightness at %3.3f" % old_brightness)

    return new_img
