import random, string

def make_txt(length):
    "makes a random string of a given length"
    return "".join(random.choices(string.printable, k=length))

def get_substring(s, num):
    "gets a substring"
    return "".join(random.choices(s, k=num))

def a(text, replace): # one of the better performing approaches from the accepted answer
    for i in replace:
        if i in text:
             text = text.replace(i, "")

def b(text, replace):
    _ = (text := text.replace(i, "") for i in replace if i in text) 


def compare(strlen, replace_length):
    "use ipython / jupyter for the %timeit functionality"

    times_a, times_b = [], []

    for i in range(*strlen):
        el = make_txt(i)
        et = get_substring(el, replace_length)

        res_a = %timeit -n 1000 -o a(el, et) # ipython magic

        el = make_txt(i)
        et = get_substring(el, replace_length)
        
        res_b = %timeit -n 1000 -o b(el, et) # ipython magic

        times_a.append(res_a.average * 1e6)
        times_b.append(res_b.average * 1e6)
        
    return times_a, times_b

#----run
t2 = compare((2*2, 1000, 50), 2)
t10 = compare((2*10, 1000, 50), 10)
