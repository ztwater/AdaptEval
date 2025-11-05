def createRawTextNode(data):
    '''
    helper function for minidom.Document:1519 to create Nodes of RawText
    see minidom.Document.createTextNode:1656
    '''
    if not isinstance(data, str):
        raise TypeError('node contents must be a string')
    r = RawText()
    r.data = data
    r.ownerDocument = dom  # there is no self
    return r

# ... and attach the helper function
dom.createRawTextNode = createRawTextNode
