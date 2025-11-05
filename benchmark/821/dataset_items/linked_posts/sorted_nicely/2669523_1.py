data = set(['booklet', '4 sheets', '48 sheets', '12 sheets'])
r = sorted(data, key=lambda item: (int(item.partition(' ')[0])
                                   if item[0].isdigit() else float('inf'), item))
print ',\n'.join(r)
