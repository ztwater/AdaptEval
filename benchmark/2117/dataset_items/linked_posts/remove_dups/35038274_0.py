text = "ask not what your country can do for you ask what you can do for your country"
sentence = text.split(" ")
noduplicates = [(sentence[i]) for i in range (0,len(sentence)) if sentence[i] not in sentence[:i]]
print(noduplicates)
