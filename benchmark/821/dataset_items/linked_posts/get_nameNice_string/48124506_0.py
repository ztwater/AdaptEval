def convert(camel_str):
    temp_list = []
    for letter in camel_str:
        if letter.islower():
            temp_list.append(letter)
        else:
            temp_list.append('_')
            temp_list.append(letter)
    result = "".join(temp_list)
    return result.lower()
