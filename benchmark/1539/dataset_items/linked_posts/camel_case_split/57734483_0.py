def camel_case_split(identifier, remove_single_letter_words=False):
    """Parses CamelCase and Snake naming"""
    concat_words = re.split('[^a-zA-Z]+', identifier)

    def camel_case_split(string):
        bldrs = [[string[0].upper()]]
        string = string[1:]
        for idx, c in enumerate(string):
            if bldrs[-1][-1].islower() and c.isupper():
                bldrs.append([c])
            elif c.isupper() and (idx+1) < len(string) and string[idx+1].islower():
                bldrs.append([c])
            else:
                bldrs[-1].append(c)

        words = [''.join(bldr) for bldr in bldrs]
        words = [word.lower() for word in words]
        return words
    words = []
    for word in concat_words:
        if len(word) > 0:
            words.extend(camel_case_split(word))
    if remove_single_letter_words:
        subset_words = []
        for word in words:
            if len(word) > 1:
                subset_words.append(word)
        if len(subset_words) > 0:
            words = subset_words
    return words
