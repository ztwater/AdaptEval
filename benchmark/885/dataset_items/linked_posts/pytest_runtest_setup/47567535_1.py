def pytest_addoption(parser):
    parser.addoption("--no_cmd", action="store_true",
                     help="run the tests only in case of that command line (marked with marker @no_cmd)")

def pytest_runtest_setup(item):
    if 'no_cmd' in item.keywords and not item.config.getoption("--no_cmd"):
        pytest.skip("need --no_cmd option to run this test")
