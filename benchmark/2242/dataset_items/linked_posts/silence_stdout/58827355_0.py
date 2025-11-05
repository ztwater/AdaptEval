import sys

class NonWritable:
    def write(self, *args, **kwargs):
        pass

class StdoutIgnore:
    def __enter__(self):
        self.stdout_saved = sys.stdout
        sys.stdout = NonWritable()
        return self

    def __exit__(self, *args):
        sys.stdout = self.stdout_saved

with StdoutIgnore():
    print("This won't print!")
