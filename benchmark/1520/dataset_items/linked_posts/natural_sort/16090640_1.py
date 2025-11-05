lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split('(\d+)', s)]
