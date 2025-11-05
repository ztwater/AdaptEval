def splitWords(s):
    new_s = re.sub(r'[^a-zA-Z0-9]', ' ',                  # not alphanumeric
        re.sub(r'([0-9]+)([^0-9])', '\\1 \\2',            # digit followed by non-digit
            re.sub(r'([a-z])([A-Z])','\\1 \\2',           # lower case followed by upper case
                re.sub(r'([A-Z])([A-Z][a-z])', '\\1 \\2', # upper case followed by upper case followed by lower case
                    s
                )
            )
        )
    )
    return [x for x in new_s.split(' ') if x]
