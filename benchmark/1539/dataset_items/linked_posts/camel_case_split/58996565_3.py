def test():
    for (q,a) in TESTS:
        r = list(camel_case_split(q))
        print(q,a,r)
        assert r == a
