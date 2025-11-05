b = set(['booklet', '10-b40', 'z94 boots', '4 sheets', '48 sheets',
         '12 sheets', '1 thing', '4a sheets', '4b sheets', '2temptations'])

numList = sorted([x for x in b if x.split(' ')[0].isdigit()],
                 key=lambda x: int(x.split(' ')[0]))

alphaList = sorted([x for x in b if not x.split(' ')[0].isdigit()])

sortedList = numList + alphaList

print(sortedList)

Out: ['1 thing',
      '4 sheets',
      '12 sheets',
      '48 sheets',
      '10-b40',
      '2temptations',
      '4a sheets',
      '4b sheets',
      'booklet',
      'z94 boots']
