import pytest


@pytest.mark.class_marker
class TestClass:
    @pytest.mark.my_test
    @pytest.mark.xfail
    def test_foo(self,request):
        print(request.instance.test_marker) #output :  ['xfail', 'my_test', 'class_marker']

    @pytest.mark.my_test_two
    @pytest.mark.xfail
    def test_foo_two(self,request):
        print(request.instance.test_marker) #output :  ['xfail', 'my_test_two', 'class_marker']
