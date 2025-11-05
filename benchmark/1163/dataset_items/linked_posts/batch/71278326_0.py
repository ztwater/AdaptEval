class my_dict:
    pass

person = my_dict()
person.id = 1 # create using dot notation
person.phone = 9999
del person.phone # Remove a property using dot notation

name_data = my_dict()
name_data.first_name = 'Arnold'
name_data.last_name = 'Schwarzenegger'

person.name = name_data
person.name.first_name # dot notation access for nested properties - gives Arnold
