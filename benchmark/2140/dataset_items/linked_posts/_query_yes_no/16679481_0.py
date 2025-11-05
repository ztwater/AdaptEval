def yes(prompt = 'Please enter Yes/No: '):
while True:
    try:
        i = raw_input(prompt)
    except KeyboardInterrupt:
        return False
    if i.lower() in ('yes','y'): return True
    elif i.lower() in ('no','n'): return False
