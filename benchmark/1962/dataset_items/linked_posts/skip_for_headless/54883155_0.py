import pytest

@pytest.fixture(scope='session')
def requires_something(request):
    something = 'a_thing'
    if request.param != something:
        pytest.skip(f"Test requires {request.param} but environment has {something}")


@pytest.mark.parametrize('requires_something',('something_else',), indirect=True)
def test_indirect(requires_something):
    print("Executing test: test_indirect")

