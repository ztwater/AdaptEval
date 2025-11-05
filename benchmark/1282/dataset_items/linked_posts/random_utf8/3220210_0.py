pattern = re.compile("[\uD800-\uDFFF].", re.UNICODE)
pattern = re.compile("[^\u0000-\uFFFF]", re.UNICODE)
