import numpy as np
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Specify a .flo file on the command line.')
    else:
        with open(sys.argv[1], 'rb') as f:
            magic, = np.fromfile(f, np.float32, count=1)
            if 202021.25 != magic:
                print('Magic number incorrect. Invalid .flo file')
            else:
                w, h = np.fromfile(f, np.int32, count=2)
                print(f'Reading {w} x {h} flo file')
                data = np.fromfile(f, np.float32, count=2*w*h)
                # Reshape data into 3D array (columns, rows, bands)
                data2D = np.resize(data, (w, h, 2))
                print(data2D)
