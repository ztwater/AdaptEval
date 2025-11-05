def remove_comments(var_0):
    var_1 = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    # first group captures quoted strings (double or single)
    # second group captures comments (//single-line or /* multi-line */)
    var_2 = re.compile(var_1, re.MULTILINE|re.DOTALL)
    def _replacer(var_3):
        # if the 2nd group (capturing comments) is not None,
        # it means we have captured a non-quoted (real) comment string.
        if var_3.group(2) is not None:
            return "" # so we will return empty to remove the comment
        else: # otherwise, we will return the 1st group
            return var_3.group(1) # captured quoted-string
    return var_2.sub(_replacer, var_0)
