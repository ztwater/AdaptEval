def ab(text):
    for ch in ['\\','`','*','_','{','}','[',']','(',')','>','#','+','-','.','!','$','\'']:
        text = text.replace(ch,"\\"+ch)


def ba(text):
    chars = "\\`*_{}[]()>#+-.!$"
    for c in chars:
        if c in text:
            text = text.replace(c, "\\" + c)
