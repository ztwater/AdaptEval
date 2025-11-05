words = ["this", "is", "an", "example"]

def get_sliding_windows(doc, sliding_window, padded=False):
    all_windows = []
    for i in range(sliding_window):
        front = sliding_window-i
        all_windows.append(front*['']+doc+i*[''])
    if padded:
        return np.array(all_windows).transpose()[1:]
    else:
        return np.array(all_windows).transpose()[sliding_window:-1]

>>> get_sliding_windows(words,3)
>>> array([['this', 'is', 'an'],
       ['is', 'an', 'example'],
       ['an', 'example', '']], dtype='<U7')

>>> get_padded_sliding_windows(words,3, True)
>>> array([['', '', 'this'],
       ['', 'this', 'is'],
       ['this', 'is', 'an'],
       ['is', 'an', 'example'],
       ['an', 'example', ''],
       ['example', '', '']], dtype='<U7')
