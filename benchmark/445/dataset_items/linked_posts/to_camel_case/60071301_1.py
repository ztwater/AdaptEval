def toCamel(escaped_snake)
    return ''.join( (word.capitalize(), '_')[word=='')
                    for word in escaped_snake.split('_') )
