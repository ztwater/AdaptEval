my_json = {'details' : {'first_name' : 'holla', 'last_name' : 'holla'}}
print(get_json_value_at_path(my_json, 'details.first_name', ''))
print(get_json_value_at_path(my_json, 'details.phone', ''))
