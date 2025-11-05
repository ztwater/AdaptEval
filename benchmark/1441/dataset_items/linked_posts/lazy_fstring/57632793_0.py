class FL:
    def __init__(self, func):
        self.func = func
    def __str__(self):
        return self.func()


template_a = FL(lambda: f"The current name, number is {name!r}, {number+1}")
names = "foo", "bar"
numbers = 40, 41
for name, number in zip(names, numbers):
    print(template_a)
