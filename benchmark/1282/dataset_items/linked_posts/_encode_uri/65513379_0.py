def replacemany(our_str, to_be_replaced:tuple, replace_with:str):
    for nextchar in to_be_replaced:
        our_str = our_str.replace(nextchar, replace_with)
    return our_str

os = 'the rain in spain falls mainly on the plain ttttttttt sssssssssss nnnnnnnnnn'
tbr = ('a','t','s','n')
rw = ''

print(replacemany(os,tbr,rw))
