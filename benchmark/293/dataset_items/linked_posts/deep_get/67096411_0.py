from contextlib import suppress

with suppress(KeyError):
    a1 = json_obj['key1']['key2']['key3']
    a2 = json_obj['key4']['key5']['key6']
    a3 = json_obj['key7']['key8']['key9']
