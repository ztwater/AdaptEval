imports sys

def redirect_output(func, output=None):
    if output is None:
        output = sys.stderr
    if isinstance(output, basestring):
        output = open(output, 'w') # etc...
    # everything else...
