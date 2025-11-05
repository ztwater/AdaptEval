def to_snake_case(s):
    snake = "".join(["_"+c.lower() if c.isupper() else c for c in s])
    return snake[1:] if snake.startswith("_") else snake
