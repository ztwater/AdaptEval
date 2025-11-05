durations = []
counter   = 0

for bool in b:
    if bool:
        counter += 1
    elif counter > 0:
        durations.append(counter)
        counter = 0

if counter > 0:
    durations.append(counter)
