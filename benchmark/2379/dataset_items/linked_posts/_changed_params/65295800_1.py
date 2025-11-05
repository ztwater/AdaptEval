d = pprint.pformat(data)
print re.sub(r'(\b\d+)L', lambda x: "0x{:x}".format(int(x.group(1))), d)
