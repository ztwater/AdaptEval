...
xfail                                      [100%]['parametrize', 'xfail', 'foo']

get_marks = ['parametrize', 'xfail', 'foo'], number = 3

    @pytest.mark.parametrize('number', [1, 2, 3])
    @pytest.mark.foo
    @pytest.mark.xfail
    def test_marks(get_marks, number):
        print(get_marks)
        assert 'xfail' in get_marks
>       assert number == 42
E       assert 3 == 42
