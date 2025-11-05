import time

# A List of Items
items = list(range(0, 57))

# A Nicer, Single-Call Usage
for item in progressBar(items, prefix = 'Progress:', suffix = 'Complete', length = 50):
    # Do stuff...
    time.sleep(0.1)
