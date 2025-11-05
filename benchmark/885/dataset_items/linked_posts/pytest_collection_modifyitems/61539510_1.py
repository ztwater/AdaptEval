def pytest_addoption(parser):
    parser.addoption('--slow-last', action='store_true', default=False)


def pytest_collection_modifyitems(items, config):
    if config.getoption('--slow-last'):
        items.sort(key=by_slow_marker, reverse=True)
