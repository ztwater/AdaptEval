import pytest


@pytest.fixture
def get_marks(request):
    marks = [m.name for m in request.node.iter_markers()]
    if request.node.parent:
        marks += [m.name for m in request.node.parent.iter_markers()]
    yield marks


@pytest.mark.parametrize('number', [1, 2, 3])
@pytest.mark.foo
@pytest.mark.xfail
def test_marks(get_marks, number):
    print(get_marks)
    assert 'xfail' in get_marks
    assert number == 42
