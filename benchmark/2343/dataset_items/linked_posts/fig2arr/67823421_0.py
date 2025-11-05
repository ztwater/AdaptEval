import io
import matplotlib
matplotlib.use('agg')  # turn off interactive backend
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot(range(10))


def plot1():
    fig.canvas.draw()
    data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    w, h = fig.canvas.get_width_height()
    im = data.reshape((int(h), int(w), -1))


def plot2():
    with io.BytesIO() as buff:
        fig.savefig(buff, format='png')
        buff.seek(0)
        im = plt.imread(buff)


def plot3():
    with io.BytesIO() as buff:
        fig.savefig(buff, format='raw')
        buff.seek(0)
        data = np.frombuffer(buff.getvalue(), dtype=np.uint8)
    w, h = fig.canvas.get_width_height()
    im = data.reshape((int(h), int(w), -1))
