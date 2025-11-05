def toCamel(esCAPed_snake)
    words = esCAPed_snake.split('_')
    return words[0].lower() + ''.join( (word.capitalize(), '_')[word=='')
                                       for word in words[1:] )
