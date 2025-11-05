pattern = re.compile(r'(?<!^)(?=[A-Z])')
name = pattern.sub('_', name).lower()
