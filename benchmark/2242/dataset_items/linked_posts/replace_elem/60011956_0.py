for i, element in enumerate(parent):
    if is_the_one_you_want_to_replace(element):
        parent.remove(element)
        parent.insert(i, new_element)
        break
