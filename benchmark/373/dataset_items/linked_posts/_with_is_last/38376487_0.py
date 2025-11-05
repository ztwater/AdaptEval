while True:
    element = element_list.pop(0)
    do_this_for_all_elements()
    if not element:
        do_this_only_for_last_element()
        break
    do_this_for_all_elements_but_last()
