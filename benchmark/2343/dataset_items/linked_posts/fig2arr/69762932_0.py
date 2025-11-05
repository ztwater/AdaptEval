from moviepy.video.io.bindings import mplfig_to_npimage
import matplotlib.pyplot as plt

fig = plt.figure()  # make a figure
numpy_fig = mplfig_to_npimage(fig)  # convert it to a numpy array
