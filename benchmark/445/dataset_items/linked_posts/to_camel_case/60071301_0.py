def toCamel(snake)
    return ''.join( word.capitalize()
                    for word in snake.split('_') )
