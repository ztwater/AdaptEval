import numpy as np
from typing import Any

Array = Any

def bmatrix(a: Array) -> str:
    r"""
    Returns a :math:`\LaTeX` bmatrix.

    :Example:

    >>> gate = tc.gates.r_gate()
    >>> array = tc.gates.matrix_for_gate(gate)
    >>> array
    array([[1.+0.j, 0.+0.j],
        [0.+0.j, 1.+0.j]], dtype=complex64)
    >>> print(tc.gates.bmatrix(array))
    \begin{bmatrix}    1.+0.j & 0.+0.j\\    0.+0.j & 1.+0.j \end{bmatrix}

    Formatted Display:

    .. math::
        \begin{bmatrix}    1.+0.j & 0.+0.j\\    0.+0.j & 1.+0.j \end{bmatrix}

    :param a: 2D numpy array
    :type a: np.array
    :raises ValueError: ValueError("bmatrix can at most display two dimensions")
    :return: :math:`\LaTeX`-formatted string for bmatrix of the array a
    :rtype: str
    """
    #   Adopted from https://stackoverflow.com/questions/17129290/numpy-2d-and-1d-array-to-latex-bmatrix/17131750

    if len(a.shape) > 2:
        raise ValueError("bmatrix can at most display two dimensions")
    # temp_string = np.array2string(a, formatter={'float_kind':lambda x: "{:.2e}".format(x)})
    # lines = temp_string.replace("[", "").replace("]", "").splitlines()
    lines = str(a).replace("[", "").replace("]", "").splitlines()
    rv = [r"\begin{bmatrix}"]
    rv += ["    " + " & ".join(l.split()) + r"\\" for l in lines]
    rv[-1] = rv[-1][:-2]
    rv += [r" \end{bmatrix}"]
    return "".join(rv)
