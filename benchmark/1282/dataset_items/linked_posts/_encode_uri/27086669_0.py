def a(text):
    chars = "&#"
    for c in chars:
        text = text.replace(c, "\\" + c)


def b(text):
    for ch in ['&','#']:
        if ch in text:
            text = text.replace(ch,"\\"+ch)


import re
def c(text):
    rx = re.compile('([&#])')
    text = rx.sub(r'\\\1', text)


RX = re.compile('([&#])')
def d(text):
    text = RX.sub(r'\\\1', text)


def mk_esc(esc_chars):
    return lambda s: ''.join(['\\' + c if c in esc_chars else c for c in s])
esc = mk_esc('&#')
def e(text):
    esc(text)


def f(text):
    text = text.replace('&', '\&').replace('#', '\#')


def g(text):
    replacements = {"&": "\&", "#": "\#"}
    text = "".join([replacements.get(c, c) for c in text])


def h(text):
    text = text.replace('&', r'\&')
    text = text.replace('#', r'\#')


def i(text):
    text = text.replace('&', r'\&').replace('#', r'\#')
