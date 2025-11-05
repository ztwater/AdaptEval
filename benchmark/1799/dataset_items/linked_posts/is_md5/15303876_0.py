    validHash = re.finditer(r'(?=(\b[A-Fa-f0-9]{32}\b))', datahere)

    result = [match.group(1) for match in validHash]

    if result: 

        print "Valid MD5"

    else:

        print "NOT a Valid MD5"
