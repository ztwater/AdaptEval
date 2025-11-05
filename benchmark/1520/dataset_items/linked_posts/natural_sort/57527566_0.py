def natsorted(seq, key=None):
    def convert(text):
        return int(text) if text.isdigit() else text

    def alphanum(obj):
        if key is not None:
            return [convert(c) for c in re.split(r'([0-9]+)', key(obj))]
        return [convert(c) for c in re.split(r'([0-9]+)', obj)]

    return sorted(seq, key=alphanum)
