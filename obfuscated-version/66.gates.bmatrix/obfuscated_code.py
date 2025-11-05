def bmatrix(var_0):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(var_0.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    var_1 = np.array2string(var_0, formatter={'float_kind':lambda x: "{:.2e}".format(x)})
    var_2 = var_1.replace('[', '').replace(']', '').splitlines()
    var_3 = [r'\begin{bmatrix}']
    var_3 += ['  ' + ' & '.join(l.split()) + r'\\' for l in var_2]
    var_3 +=  [r'\end{bmatrix}']
    return '\n'.join(var_3)
