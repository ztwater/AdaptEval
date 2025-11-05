from collections import deque
def window(seq, n=2):
    it = iter(seq)
    win = deque((next(it, None) for _ in xrange(1)), maxlen=n)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win
    for _ in xrange(len(win)-1):
        win.popleft()
        yield win

for wnd in window(range(5), n=3):
    print(list(wnd))
