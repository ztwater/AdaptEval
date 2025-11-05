a = ['H1', 'H100', 'H10', 'H3', 'H2', 'H6', 'H11', 'H50', 'H5', 'H99', 'H8']
b = ''
c = []

def bubble(bad_list):#bubble sort method
        length = len(bad_list) - 1
        sorted = False

        while not sorted:
                sorted = True
                for i in range(length):
                        if bad_list[i] > bad_list[i+1]:
                                sorted = False
                                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i] #sort the integer list 
                                a[i], a[i+1] = a[i+1], a[i] #sort the main list based on the integer list index value

for a_string in a: #extract the number in the string character by character
        for letter in a_string:
                if letter.isdigit():
                        #print letter
                        b += letter
        c.append(b)
        b = ''

print 'Before sorting....'
print a
c = map(int, c) #converting string list into number list
print c
bubble(c)

print 'After sorting....'
print c
print a
