import yaml
from collections import OrderedDict

def ordered_load(var_0, var_1=yaml.SafeLoader, var_2=OrderedDict):
    class OrderedLoader(var_1):
        pass
    def construct_mapping(var_3, var_4):
        var_3.flatten_mapping(var_4)
        return var_2(var_3.construct_pairs(var_4))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(var_0, OrderedLoader)
 
