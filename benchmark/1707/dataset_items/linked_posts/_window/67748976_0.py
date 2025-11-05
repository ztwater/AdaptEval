from collections import deque

def window(ls,window_size=3):
    window = deque(maxlen=window_size)

    for element in ls:
        
        if len(window)==window_size:
            yield list(window)
        window.append(element)

ls = [0,1,2,3,4,5]

for w in window(ls):
    print(w)
