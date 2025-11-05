import subprocess
import string

#define alphabet
alphabet = []
for i in string.ascii_uppercase:
    alphabet.append(i + ':')

#get letters that are mounted somewhere
mounted_letters = subprocess.Popen("wmic logicaldisk get name", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#erase mounted letters from alphabet in nested loop
for line in mounted_letters.stdout.readlines():
    if "Name" in line:
        continue
    for letter in alphabet:
        if letter in line:
            print 'Deleting letter %s from free alphabet %s' % letter
            alphabet.pop(alphabet.index(letter))

print alphabet
