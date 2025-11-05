def ab_with_check(text):
    for ch in ['\\','`','*','_','{','}','[',']','(',')','>','#','+','-','.','!','$','\'']:
        if ch in text:
            text = text.replace(ch,"\\"+ch)

def ba_without_check(text):
    chars = "\\`*_{}[]()>#+-.!$"
    for c in chars:
        text = text.replace(c, "\\" + c)
