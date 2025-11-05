from scipy import interpolate

if __name__ == '__main__':
    x = [ 0, 1, 2, 3, 4, 5]
    y = [12,14,22,39,58,77]

    # tck : tuple (t,c,k) a tuple containing the vector of knots,
    # the B-spline coefficients, and the degree of the spline.
    tck = interpolate.splrep(x, y)

    print(interpolate.splev(1.25, tck)) # Prints 15.203125000000002
    print(interpolate.splev(...other_value_here..., tck))
