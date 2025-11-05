roman_conver=[  (1,'I'),
                (5,'V'),
                (10,'X'),
                (50,'L'),
                (100,'C'),
                (500,'D'),
                (1000,'M'),
                    ]
def romantonumeral(roman):
    tot = 0
    for i in range(0,len(roman)):
        for each in roman_conver:
            if roman[i]==each[1]:
                if each[0]>tot:
                    tot = each[0] - tot
                else:
                    tot = tot + each[0]
    return tot
