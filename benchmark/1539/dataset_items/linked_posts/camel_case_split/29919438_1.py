def camel_case_split2(string):
    # set the logic for creating a "break"
    def is_transition(c1, c2):
      return c1.islower() and c2.isupper()

    # start the builder list with the first character
    # enforce upper case
    bldr = [string[0].upper()]
    for c in string[1:]:
        # get the last character in the last element in the builder
        # note that strings can be addressed just like lists
        previous_character = bldr[-1][-1]
        if is_transition(previous_character, c):
            # start a new element in the list
            bldr.append(c)
        else:
            # append the character to the last string
            bldr[-1] += c
    return bldr
