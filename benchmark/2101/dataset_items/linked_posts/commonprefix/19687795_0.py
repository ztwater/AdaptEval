def common_prefix(strings):

    if len(strings) == 1:#rule out trivial case
        return strings[0]

    prefix = strings[0]

    for string in strings[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix)-1]
        if not prefix:
            break

    return prefix

strings = ["my_prefix_what_ever","my_prefix_what_so_ever","my_prefix_doesnt_matter"]

print common_prefix(strings)
#Prints "my_prefix_"
