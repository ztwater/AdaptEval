from subprocess import check_output

#for windows & linux
hash = check_output(args='md5sum imp_file.txt', shell=True).decode().split(' ')[0]

#for mac
hash = check_output(args='md5 imp_file.txt', shell=True).decode().split('=')[1]
