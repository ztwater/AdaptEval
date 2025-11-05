def by_slow_marker(item):
    return 0 if item.get_closest_marker("slow") is None else 1

def pytest_collection_modifyitems(session, config, items):
    if config.getoption("--slow-last"):
        items.sort(key=by_slow_marker, reverse=False)

def pytest_addoption(parser, pluginmanager):
    parser.addoption("--slow-last", action="store_true", default=False)
