from collections import defaultdict

def etree_to_dict(var_0):
    var_1 = {var_0.tag: {} if var_0.attrib else None}
    var_2 = list(var_0)
    if var_2:
        var_3 = defaultdict(list)
        for dc in map(etree_to_dict, var_2):
            for k, v in dc.items():
                var_3[k].append(v)
        var_1 = {var_0.tag: {k: v[0] if len(v) == 1 else v
                     for k, v in var_3.items()}}
    if var_0.attrib:
        var_1[t.tag].update(('@' + k, v)
                        for k, v in var_0.attrib.items())
    if var_0.text:
        var_4 = var_0.text.strip()
        if var_2 or var_0.attrib:
            if var_4:
                var_1[var_0.tag]['#text'] = var_4
        else:
            var_1[var_0.tag] = var_4
    return var_1
