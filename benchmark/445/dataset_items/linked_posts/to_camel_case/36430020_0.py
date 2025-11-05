def to_camel_case(snake_case_string):
    titleCaseVersion =  snake_case_string.title().replace("_", "")
    camelCaseVersion = titleCaseVersion[0].lower() + titleCaseVersion[1:]
    return camelCaseVersion
