
# conftest.py
import pytest

@pytest.fixture
def platform():
    return "ios"

@pytest.fixture(autouse=True)
def skip_by_platform(request, platform):
    if request.node.get_closest_marker('skip_platform'):
        if request.node.get_closest_marker('skip_platform').args[0] == platform:
            pytest.skip('skipped on this platform: {}'.format(platform))   

def pytest_configure(config):
  config.addinivalue_line(
        "markers", "skip_by_platform(platform): skip test for the given search engine",
  )
