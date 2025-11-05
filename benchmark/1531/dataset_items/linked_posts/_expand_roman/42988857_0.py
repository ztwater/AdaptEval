def rome(roman_num):
     d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
     nl = list(roman_num)
     sum = d[nl[len(nl)-1]]
     for i in range(len(nl)-1,0,-1):
             if d[nl[i]]>d[nl[i-1]]:
                     sum -= d[nl[i-1]]
             else:
                     sum += d[nl[i-1]]       
     return sum
