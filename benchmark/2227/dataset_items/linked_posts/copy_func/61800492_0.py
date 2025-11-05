from a import x as xx

# Define globals for the function here
glob = {'value': 4}
def x():
    return eval(xx.__code__, glob)

