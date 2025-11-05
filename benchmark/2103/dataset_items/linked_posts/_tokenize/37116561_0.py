class FortranAsciiReader(file):

def read(self, *args):
    """
    Read from file into the given objects
    """
    num_args = len(args)
    num_read = 0
    encountered_slash = False
    # If line contained '/' or read into all varialbes, we're done
    while num_read < num_args and not encountered_slash:
        line = self.readline()
        if not line:
            raise Exception()
        values = tokenize(line)
        # Assign elements one-by-one into args, skipping empty fields and stopping at a '/'
        for val in values:
            if val == '/':
                encountered_slash = True
                break
            elif val == '':
                num_read += 1
            else:
                args[num_read].assign(val)
                num_read += 1
                if num_read == num_args:
                    break
