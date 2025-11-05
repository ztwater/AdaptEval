a = "SomeCamelTextUpper"
def camelText(val):
    return ''.join([' ' + i if i.isupper() else i for i in val]).strip()
print(camelText(a))
