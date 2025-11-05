def _camel_case_split_iter(string: str) -> Iterable[str]:
    previous_char_upper = True
    previous_char_digit = True
    curr_word = ""
    upper_buffer = ""  # buffer for last uppercase letter
    for c in string:
        curr_char_upper = c.isupper()
        curr_char_digit = c.isdigit()
        if c.isspace() or c in ["_", "."]:
            if len(curr_word) > 0 or len(upper_buffer) > 0:
                yield curr_word + upper_buffer
                curr_word = upper_buffer = ""
        elif previous_char_upper and curr_char_upper:
            curr_word += upper_buffer
            upper_buffer = c
        elif previous_char_upper and not curr_char_upper and not curr_char_digit:
            if len(curr_word) > 0:
                yield curr_word
            curr_word = upper_buffer + c
            upper_buffer = ""
        elif not previous_char_upper and curr_char_upper:
            if len(curr_word) > 0:
                yield curr_word
                curr_word = ""
            upper_buffer = c
        elif (not previous_char_digit and curr_char_digit) or (previous_char_digit and not curr_char_digit):
            if len(curr_word) > 0 or len(upper_buffer) > 0:
                yield curr_word + upper_buffer
                upper_buffer = ""
            curr_word = c
        else:
            curr_word += c
        previous_char_upper = curr_char_upper
        previous_char_digit = curr_char_digit
    if len(curr_word) > 0 or len(upper_buffer) > 0:  # flush
        yield curr_word + upper_buffer


def camel_case_split(string: str) -> list[str]:
    """
    Split CamelCase string to words.

    >>> camel_case_split("XYZCamelCaseXYZ")
    ['XYZ', 'Camel', 'Case', 'XYZ']
    >>> camel_case_split("Ta")
    ['Ta']
    >>> camel_case_split("aT")
    ['a', 'T']
    >>> camel_case_split("_aAa_bBb__CCC__")
    ['a', 'Aa', 'b', 'Bb', 'CCC']
    >>> camel_case_split("10Camel20CaseXYZ30")
    ['10', 'Camel', '20', 'Case', 'XYZ', '30']
    >>> camel_case_split(" CamelCase camel case ")
    ['Camel', 'Case', 'camel', 'case']
    """
    return list(_camel_case_split_iter(string))
