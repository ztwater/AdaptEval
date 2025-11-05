#!/usr/bin/env python3
# keywords: nearest-neighbor regular-grid python numpy searchsorted Voronoi

import numpy as np

#...............................................................................
class Near_rgrid( object ):
    """ nearest neighbors on a Manhattan aka regular grid
    1d:
    near = Near_rgrid( x: sorted 1d array )
    nearix = near.query( q: 1d ) -> indices of the points x_i nearest each q_i
        x[nearix[0]] is the nearest to q[0]
        x[nearix[1]] is the nearest to q[1] ...
        nearpoints = x[nearix] is near q
    If A is an array of e.g. colors at x[0] x[1] ...,
    A[nearix] are the values near q[0] q[1] ...
    Query points < x[0] snap to x[0], similarly > x[-1].

    2d: on a Manhattan aka regular grid,
        streets running east-west at y_i, avenues north-south at x_j,
    near = Near_rgrid( y, x: sorted 1d arrays, e.g. latitide longitude )
    I, J = near.query( q: nq × 2 array, columns qy qx )
    -> nq × 2 indices of the gridpoints y_i x_j nearest each query point
        gridpoints = np.column_stack(( y[I], x[J] ))  # e.g. street corners
        diff = gridpoints - querypoints
        distances = norm( diff, axis=1, ord= )
    Values at an array A definded at the gridpoints y_i x_j nearest q: A[I,J]

    3d: Near_rgrid( z, y, x: 1d axis arrays ) .query( q: nq × 3 array )

    See Howitworks below, and the plot Voronoi-random-regular-grid.
    """

    def __init__( self, *axes: "1d arrays" ):
        axarrays = []
        for ax in axes:
            axarray = np.asarray( ax ).squeeze()
            assert axarray.ndim == 1, "each axis should be 1d, not %s " % (
                    str( axarray.shape ))
            axarrays += [axarray]
        self.midpoints = [_midpoints( ax ) for ax in axarrays]
        self.axes = axarrays
        self.ndim = len(axes)

    def query( self, queries: "nq × dim points" ) -> "nq × dim indices":
        """ -> the indices of the nearest points in the grid """
        queries = np.asarray( queries ).squeeze()  # or list x y z ?
        if self.ndim == 1:
            assert queries.ndim <= 1, queries.shape
            return np.searchsorted( self.midpoints[0], queries )  # scalar, 0d ?
        queries = np.atleast_2d( queries )
        assert queries.shape[1] == self.ndim, [
                queries.shape, self.ndim]
        return [np.searchsorted( mid, q )  # parallel: k axes, k processors
                for mid, q in zip( self.midpoints, queries.T )]

    def snaptogrid( self, queries: "nq × dim points" ):
        """ -> the nearest points in the grid, 2d [[y_j x_i] ...] """
        ix = self.query( queries )
        if self.ndim == 1:
            return self.axes[0][ix]
        else:
            axix = [ax[j] for ax, j in zip( self.axes, ix )]
            return np.array( axix )


def _midpoints( points: "array-like 1d, *must be sorted*" ) -> "1d":
    points = np.asarray( points ).squeeze()
    assert points.ndim == 1, points.shape
    diffs = np.diff( points )
    assert np.nanmin( diffs ) > 0, "the input array must be sorted, not %s " % (
            points.round( 2 ))
    return (points[:-1] + points[1:]) / 2  # floats

#...............................................................................
Howitworks = \
"""
How Near_rgrid works in 1d:
Consider the midpoints halfway between fenceposts | | |
The interval [left midpoint .. | .. right midpoint] is what's nearest each post --

    |   |       |                     |   points
    | . |   .   |          .          |   midpoints
      ^^^^^^               .            nearest points[1]
            ^^^^^^^^^^^^^^^             nearest points[2]  etc.

2d:
    I, J = Near_rgrid( y, x ).query( q )
    I = nearest in `x`
    J = nearest in `y` independently / in parallel.
    The points nearest [yi xj] in a regular grid (its Voronoi cell)
    form a rectangle [left mid x .. right mid x] × [left mid y .. right mid y]
    (in any norm ?)
    See the plot Voronoi-random-regular-grid.

Notes
-----
If a query point is exactly halfway between two data points,
e.g. on a grid of ints, the lines (x + 1/2) U (y + 1/2),
which "nearest" you get is implementation-dependent, unpredictable.

"""

Murky = \
""" NaNs in points, in queries ?
"""

__version__ = "2021-10-25 oct  denis-bz-py"
