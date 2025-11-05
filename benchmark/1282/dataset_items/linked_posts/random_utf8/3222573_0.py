all(uc < u'\ud800' or u'\ue000' <= uc <= u'\uffff' for uc in unicode_string)
