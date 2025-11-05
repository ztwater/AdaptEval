def sliding_window(items, size):
    return [items[start:end] for start, end
            in zip(range(0, len(items) - size + 1), range(size, len(items) + 1))]
