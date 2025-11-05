@pytest.mark.usefixtures('sample_data')
def test_this(sample_data):
    nested_dict, param, update_value = sample_data

    if nested_dict is None:
        print(f'\nDict Value: Level0\nParam: {param}\nUpdate Value: {update_value}')
    else:
        print(f'\nDict Value: {nested_dict}\nParam: {param}\nUpdate Value: {update_value}')

    # initialise data dict
    data_object = # insert data here (see example dict above)

    # first print as is
    print(f'\nOriginal Dict:\n{data_object}')

    update(dictionary=data_object,
           key=param,
           value=update_value,
           nested_dict_name=nested_dict)

    # print updated
    print(f'\nUpdated Dict:\n{data_object}')
