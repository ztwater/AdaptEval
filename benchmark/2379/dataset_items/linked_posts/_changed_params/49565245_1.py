>>> sample = {66: 'far',
...  99: 'Bottles of the beer on the wall',
...  '12': 4277009102,
...  'boo': 21,
...  'pprint': [16, 32, 48, 64, 80, 96, 112, 128]}
>>> pprinter = HexIntPrettyPrinter()
>>> pprinter.pprint(sample)
{0x42: 'far',
 0x63: 'Bottles of the beer on the wall',
 '12': 0xFEEDFACE,
 'boo': 0x15,
 'pprint': [0x10, 0x20, 0x30, 0x40, 0x50, 0x60, 0x70, 0x80]}
