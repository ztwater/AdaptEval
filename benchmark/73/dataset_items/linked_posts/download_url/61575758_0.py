import urllib
from tqdm.auto import tqdm

class TqdmUpTo(tqdm):
    """Provides `update_to(n)` which uses `tqdm.update(delta_n)`."""
    def update_to(self, b=1, bsize=1, tsize=None):
        """
        b  : Blocks transferred so far
        bsize  : Size of each block
        tsize  : Total size
        """
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)  # will also set self.n = b * bsize

eg_link = "https://github.com/tqdm/tqdm/releases/download/v4.46.0/tqdm-4.46.0-py2.py3-none-any.whl"
eg_file = eg_link.split('/')[-1]
with TqdmUpTo(unit='B', unit_scale=True, unit_divisor=1024, miniters=1,
              desc=eg_file) as t:  # all optional kwargs
    urllib.urlretrieve(
        eg_link, filename=eg_file, reporthook=t.update_to, data=None)
    t.total = t.n
