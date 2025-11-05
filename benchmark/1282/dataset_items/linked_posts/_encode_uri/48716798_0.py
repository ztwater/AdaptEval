s = "abc&def#ghi"
print(s.translate(str.maketrans({'&': '\&', '#': '\#'})))
