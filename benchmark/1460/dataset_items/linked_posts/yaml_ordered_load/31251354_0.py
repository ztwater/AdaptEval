import yaml
import re
from collections import OrderedDict

def yaml_load_od(fname):
    "load a yaml file as an OrderedDict"
    # detects any duped keys (fail on this) and preserves order of top level keys
    with open(fname, 'r') as f:
        lines = open(fname, "r").read().splitlines()
        top_keys = []
        duped_keys = []
        for line in lines:
            m = re.search(r'^([A-Za-z0-9_]+) *:', line)
            if m:
                if m.group(1) in top_keys:
                    duped_keys.append(m.group(1))
                else:
                    top_keys.append(m.group(1))
        if duped_keys:
            raise Exception('ERROR: duplicate keys: {}'.format(duped_keys))
    # 2nd pass to set up the OrderedDict
    with open(fname, 'r') as f:
        d_tmp = yaml.load(f)
    return OrderedDict([(key, d_tmp[key]) for key in top_keys])
