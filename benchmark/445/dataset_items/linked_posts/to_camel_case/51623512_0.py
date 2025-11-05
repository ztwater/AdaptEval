def snake_to_camel_case(text_snake):
    return '{}{}'.format(
        text_snake[:1].lower(),
        text_snake.title().replace('_', '')[1:],
    )
