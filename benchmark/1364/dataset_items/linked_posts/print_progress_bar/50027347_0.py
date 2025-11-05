def progress_bar(current_value, total):
    increments = 50
    percentual = ((current_value/ total) * 100)
    i = int(percentual // (100 / increments ))
    text = "\r[{0: <{1}}] {2}%".format('=' * i, increments, percentual)
    print(text, end="\n" if percentual == 100 else "")
