data_list.reverse()
while data_list:
   value = data_list.pop()
   code_that_is_done_for_every_element(value)
   if data_list:
       code_that_is_done_between_elements(value)
   else:
       code_that_is_done_for_last_element(value)


