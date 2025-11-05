>>> canvas = np.full((256, 256, 3), 255)
>>> canvas
array([[255, 255, 255],
       [255, 255, 255],
       [255, 255, 255]])
>>> canvas.dtype
dtype('int64')
>>> cv2.rectangle(canvas, (0, 0), (2, 2), (0, 0, 0))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Layout of the output array img is incompatible with cv::Mat (step[ndims-1] != elemsize or step[1] != elemsize*nchannels)
