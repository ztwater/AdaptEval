#get output to list
mounted_letters_list = []
for line in mounted_letters.stdout.readlines():
    if "Name" in line:
        continue
    mounted_letters_list.append(line.strip())

rest = list(set(alphabet) - set(mounted_letters_list))
rest.sort()
print rest
