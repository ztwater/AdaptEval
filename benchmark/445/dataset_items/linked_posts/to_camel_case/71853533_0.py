from functools import reduce

def camelize(snake_string: str) -> str:
    return reduce(lambda x, y: x + y.capitalize(), snake_string.split('_'))
