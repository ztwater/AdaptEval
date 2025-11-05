my_list = [{'name':'b'}, {'name':'10'}, {'name':'a'}, {'name':'1'}, {'name':'9'}]
natural_sort(my_list, key=lambda x: x['name'])
print my_list
[{'name': '1'}, {'name': '9'}, {'name': '10'}, {'name': 'a'}, {'name': 'b'}]
