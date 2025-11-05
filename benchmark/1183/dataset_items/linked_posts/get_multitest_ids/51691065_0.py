class Foo:

    # A class-level variable.
    X = 10

    # I can use that variable to define another class-level variable.
    Y = sum((X, X))

    # Works in Python 2, but not 3.
    # In Python 3, list comprehensions were given their own scope.
    try:
        Z1 = sum([X for _ in range(3)])
    except NameError:
        Z1 = None

    # Fails in both.
    # Apparently, generator expressions (that's what the entire argument
    # to sum() is) did have their own scope even in Python 2.
    try:
        Z2 = sum(X for _ in range(3))
    except NameError:
        Z2 = None

    # Workaround: put the computation in lambda or def.
    compute_z3 = lambda val: sum(val for _ in range(3))

    # Then use that function.
    Z3 = compute_z3(X)

    # Also worth noting: here I can refer to XS in the for-part of the
    # generator expression (Z4 works), but I cannot refer to XS in the
    # inner-part of the generator expression (Z5 fails).
    XS = [15, 15, 15, 15]
    Z4 = sum(val for val in XS)
    try:
        Z5 = sum(XS[i] for i in range(len(XS)))
    except NameError:
        Z5 = None

print(Foo.Z1, Foo.Z2, Foo.Z3, Foo.Z4, Foo.Z5)
