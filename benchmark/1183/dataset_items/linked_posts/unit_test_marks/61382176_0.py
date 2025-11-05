import pytest

marker_name = [] #Global variable so you can use it everywhere

def pytest_runtest_setup(item):
    global marker_name
    marker_name.clear() #If you would not clear this, it would append every test's marker, test by test. 
    for mark in item.iter_markers():
        marker_name.append(mark.name)


@pytest.fixture(scope='function', autouse=True) #Note here, autouse=true.
def my_fixture(request):
    request.instance.test_marker=marker_name #assign it to request's session so you can use it in other fixture and in tests as well

@pytest.fixture
def some_other_fixture(request):
    test_marker=request.instance.test_marker #access marker in fixture
