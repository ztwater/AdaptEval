configfile = '~/config.py'

import os
import sys

sys.path.append(os.path.dirname(os.path.expanduser(configfile)))

import config
