class StaticValue:
    val = None

    def __init__(self, value: int):
        StaticValue.val = value

    @staticmethod
    def get_lambda():
        return lambda x: x*StaticValue.val


class NotStaticValue:
    def __init__(self, value: int):
        self.val = value

    def get_lambda(self):
        return lambda x: x*self.val


if __name__ == '__main__':
    def foo():
        return [lambda x: x*i for i in range(4)]

    def bar():
        return [StaticValue(i).get_lambda() for i in range(4)]

    def foo_repaired():
        return [NotStaticValue(i).get_lambda() for i in range(4)]

    print([x(2) for x in foo()])
    print([x(2) for x in bar()])
    print([x(2) for x in foo_repaired()])

Result:
[6, 6, 6, 6]
[6, 6, 6, 6]
[0, 2, 4, 6]
