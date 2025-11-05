>>> snake_case = "this_is_a_snake_case_string"
>>> l = snake_case.split("_")
>>> print l[0] + "".join(map(str.capitalize, l[1:]))
'thisIsASnakeCaseString'
