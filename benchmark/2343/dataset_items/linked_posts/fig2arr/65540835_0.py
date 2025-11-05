canvas = pyplot.gca().figure.canvas
canvas.draw()
data = numpy.frombuffer(canvas.tostring_rgb(), dtype=numpy.uint8)
image = data.reshape(canvas.get_width_height()[::-1] + (3,))
