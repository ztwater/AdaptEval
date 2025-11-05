def to_camel_case(snake_str):
    components = snake_str.split('_')
    return reduce(lambda x, y: x + y.title(), components[1:], components[0])
