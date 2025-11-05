from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4).pprint
pf = PrettyPrinter(indent=4).pformat
def pph(o):
    print(re.sub(r"((?:, +|: +|\( *|\[ *|\{ *)-?)(\d\d+)(?=[,)}\]])", lambda m: m.group(1) + hex(m.group(2)), pf(o)))
def pfh(o):
    return re.sub(r"((?:, +|: +|\( *|\[ *|\{ *)-?)(\d\d+)(?=[,)}\]])", lambda m: m.group(1) + hex(m.group(2)), pf(o))

