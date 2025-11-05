''.join('_'+c.lower() if c.isupper() else c for c in "DeathToCamelCase").strip('_')
re.sub("(.)([A-Z])", r'\1_\2', 'DeathToCamelCase').lower()
