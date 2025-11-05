class MyClass:
    def f(self):
        return 42


x = MyClass()
with patch(MyClass, 'f') as f_patcher:
    y = MyClass()  # inside or outside -- does not matter
    assert x.f() == 42
    assert f_patcher.call_count == 1
    f_patcher.return_value = 7
    assert y.f() == 7
    assert f_patcher.call_count == 2
