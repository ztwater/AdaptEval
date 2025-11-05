u''.join(
    uc if uc < u'\ud800' or u'\ue000' <= uc <= u'\uffff' else u'\ufffd'
    for uc in unicode_string
    )
