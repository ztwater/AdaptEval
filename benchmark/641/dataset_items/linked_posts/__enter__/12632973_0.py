A new statement is proposed with the syntax:

    with EXPR as VAR:
        BLOCK

....

The translation of the above statement is:

    mgr = (EXPR)
    exit = type(mgr).__exit__  # Not calling it yet
    value = type(mgr).__enter__(mgr)

....
