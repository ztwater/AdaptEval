replacement_map = {}

for i, element in enumerate(parent):
    if is_an_element_you_want_to_replace(element):
        replacement_map[i] = el_to_remove, el_to_add

for index, (el_to_remove, el_to_add) in replacement_map.items():
    parent.remove(el_to_remove)
    parent.insert(index, el_to_add)
