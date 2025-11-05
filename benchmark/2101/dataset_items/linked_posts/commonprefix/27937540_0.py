import collections
import itertools

def commonprefix(instrings):
    """ Common prefix of a list of input strings using OrderedDict """

    d = collections.OrderedDict()

    for instring in instrings:
        for idx,char in enumerate(instring):
            # Make sure index is added into key
            d[(char, idx)] = d.get((char,idx), 0) + 1

    # Return prefix of keys while value == length(instrings)
    return ''.join([k[0] for k in itertools.takewhile(lambda x: d[x] == len(instrings), d)])
