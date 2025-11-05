camelcase_to_underscore = lambda str: re.sub(r'(?<=[a-z])[A-Z]|[A-Z](?=[^A-Z])', r'_\g<0>', str).lower().strip('_')
