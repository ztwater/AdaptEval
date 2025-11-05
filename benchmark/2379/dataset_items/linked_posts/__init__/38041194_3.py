root = dom.documentElement

evil = dom.createElement('evil')
root.appendChild(evil)
evil.appendChild(dom.createTextNode(SNOWMAN))

good = dom.createElement('good')
root.appendChild(good)
# use helper function to create Nodes of RawText
good.appendChild(dom.createRawTextNode(SNOWMAN))

# yay, works! |o_0|
print(dom.toprettyxml(indent=' '))
