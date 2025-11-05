Traceback (most recent call last):
  File "D:/home/video dev/mp test/mp_test_02.py", line 86, in <module>
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv_mat)
TypeError: __init__(): incompatible constructor arguments. The following argument types are supported:
    1. mediapipe.python._framework_bindings.image.Image(image_format: mediapipe::ImageFormat_Format, data: numpy.ndarray[numpy.uint8])
    2. mediapipe.python._framework_bindings.image.Image(image_format: mediapipe::ImageFormat_Format, data: numpy.ndarray[numpy.uint16])
    3. mediapipe.python._framework_bindings.image.Image(image_format: mediapipe::ImageFormat_Format, data: numpy.ndarray[numpy.float32])

Invoked with: kwargs: image_format=<ImageFormat.SRGB: 1>, data=array([[[16, 19,  0],
        [12, 19,  3],
        [12, 19,  1],
        ...,
        [11, 18,  2],
        [14, 16,  2],
        [14, 18,  3]],
        ...,
        [29, 81, 81],
        [26, 83, 82],
        [29, 79, 91]]], dtype=uint8)
