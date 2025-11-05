def pytest_runtest_call(item):
    evalskipif = ExtendedMarkEvaluator(item, "skipif_call")
    if evalskipif.istrue():
        pytest.skip('[CANNOT RUN]' + evalskipif.getexplanation())
