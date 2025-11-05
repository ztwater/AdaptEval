def natural_sort_key(string_or_number):
    """
    by Scott S. Lawton <scott@ProductArchitect.com> 2014-12-11; public domain and/or CC0 license

    handles cases where simple 'int' approach fails, e.g.
        ['0.501', '0.55'] floating point with different number of significant digits
        [0.01, 0.1, 1]    already numeric so regex and other string functions won't work (and aren't required)
        ['elm1', 'Elm2']  ASCII vs. letters (not case sensitive)
    """

    def try_float(astring):
        try:
            return float(astring)
        except:
            return astring

    if isinstance(string_or_number, basestring):
        string_or_number = string_or_number.lower()

        if len(re.findall('[.]\d', string_or_number)) <= 1:
            # assume a floating point value, e.g. to correctly sort ['0.501', '0.55']
            # '.' for decimal is locale-specific, e.g. correct for the Anglosphere and Asia but not continental Europe
            return [try_float(s) for s in re.split(r'([\d.]+)', string_or_number)]
        else:
            # assume distinct fields, e.g. IP address, phone number with '.', etc.
            # caveat: might want to first split by whitespace
            # TBD: for unicode, replace isdigit with isdecimal
            return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_or_number)]
    else:
        # consider: add code to recurse for lists/tuples and perhaps other iterables
        return string_or_number
