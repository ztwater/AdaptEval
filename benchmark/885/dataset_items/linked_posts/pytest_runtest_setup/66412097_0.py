# content of conftest.py
 
import pytest

# Create a dict of markers.
# The key is used as option, so --{key} will run all tests marked with key.
# The value must be a dict that specifies:
# 1. 'help': the command line help text
# 2. 'marker-descr': a description of the marker
# 3. 'skip-reason': displayed reason whenever a test with this marker is skipped.
optional_markers = {
    "flag1": {"help": "<Command line help text for flag1...>",
             "marker-descr": "<Description of the marker...>",
             "skip-reason": "Test only runs with the --{} option."},
    "flag2": {"help": "<Command line help text for flag2...>",
             "marker-descr": "<Description of the marker...>",
             "skip-reason": "Test only runs with the --{} option."},
    # add further markers here
}


def pytest_addoption(parser):
    for marker, info in optional_markers.items():
        parser.addoption("--{}".format(marker), action="store_true",
                         default=False, help=info['help'])


def pytest_configure(config):
    for marker, info in optional_markers.items():
        config.addinivalue_line("markers",
                                "{}: {}".format(marker, info['marker-descr']))


def pytest_collection_modifyitems(config, items):
    for marker, info in optional_markers.items():
        if not config.getoption("--{}".format(marker)):
            skip_test = pytest.mark.skip(
                reason=info['skip-reason'].format(marker)
            )
            for item in items:
                if marker in item.keywords:
                    item.add_marker(skip_test)

