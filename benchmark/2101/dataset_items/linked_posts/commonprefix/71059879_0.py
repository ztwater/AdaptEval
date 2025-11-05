stringList = ['my_prefix_what_ever', 'my_prefix_what_so_ever', 'my_prefix_doesnt_matter']
len2 = len( stringList )
if len2 != 0:
    # let shortest word is prefix
    prefix = min( stringList )
    for i in range( len2 ):
        word = stringList[ i ]
        len1 = len( prefix )
        # slicing each word as lenght of prefix
        word = word[ 0:len1 ]
        for j in range( len1 ):
            # comparing each letter of word and prefix
            if word[ j ] != prefix[ j ]:
                # if letter does not match slice the prefix
                prefix = prefix[ :j ]
                break # after getting comman prefix move to next word
    if len( prefix ) != 0:
        print("common prefix: ",prefix)
    else:
        print("-1")
else:
     print("string List is empty") 
