for item in data_list:
    try:
        print(new)
    except NameError: pass
    new = item
print('The last item: ' + str(new))
