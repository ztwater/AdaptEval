>>> items = [1, 2, 0, 1, 3, 2]
>>> list(dict.fromkeys(items))  # Or [*dict.fromkeys(items)] if you prefer
[1, 2, 0, 3]
