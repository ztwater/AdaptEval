def a(text):
    chars = "\\`*_{}[]()>#+-.!$"
    for c in chars:
        text = text.replace(c, "\\" + c)


def b(text):
    for ch in ['\\','`','*','_','{','}','[',']','(',')','>','#','+','-','.','!','$','\'']:
        if ch in text:
            text = text.replace(ch,"\\"+ch)


import re
def c(text):
    rx = re.compile('([&#])')
    text = rx.sub(r'\\\1', text)


RX = re.compile('([\\`*_{}[]()>#+-.!$])')
def d(text):
    text = RX.sub(r'\\\1', text)


def mk_esc(esc_chars):
    return lambda s: ''.join(['\\' + c if c in esc_chars else c for c in s])
esc = mk_esc('\\`*_{}[]()>#+-.!$')
def e(text):
    esc(text)


def f(text):
    text = text.replace('\\', '\\\\').replace('`', '\`').replace('*', '\*').replace('_', '\_').replace('{', '\{').replace('}', '\}').replace('[', '\[').replace(']', '\]').replace('(', '\(').replace(')', '\)').replace('>', '\>').replace('#', '\#').replace('+', '\+').replace('-', '\-').replace('.', '\.').replace('!', '\!').replace('$', '\$')


def g(text):
    replacements = {
        "\\": "\\\\",
        "`": "\`",
        "*": "\*",
        "_": "\_",
        "{": "\{",
        "}": "\}",
        "[": "\[",
        "]": "\]",
        "(": "\(",
        ")": "\)",
        ">": "\>",
        "#": "\#",
        "+": "\+",
        "-": "\-",
        ".": "\.",
        "!": "\!",
        "$": "\$",
    }
    text = "".join([replacements.get(c, c) for c in text])


def h(text):
    text = text.replace('\\', r'\\')
    text = text.replace('`', r'\`')
    text = text.replace('*', r'\*')
    text = text.replace('_', r'\_')
    text = text.replace('{', r'\{')
    text = text.replace('}', r'\}')
    text = text.replace('[', r'\[')
    text = text.replace(']', r'\]')
    text = text.replace('(', r'\(')
    text = text.replace(')', r'\)')
    text = text.replace('>', r'\>')
    text = text.replace('#', r'\#')
    text = text.replace('+', r'\+')
    text = text.replace('-', r'\-')
    text = text.replace('.', r'\.')
    text = text.replace('!', r'\!')
    text = text.replace('$', r'\$')


def i(text):
    text = text.replace('\\', r'\\').replace('`', r'\`').replace('*', r'\*').replace('_', r'\_').replace('{', r'\{').replace('}', r'\}').replace('[', r'\[').replace(']', r'\]').replace('(', r'\(').replace(')', r'\)').replace('>', r'\>').replace('#', r'\#').replace('+', r'\+').replace('-', r'\-').replace('.', r'\.').replace('!', r'\!').replace('$', r'\$')
