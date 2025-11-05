import os

folder = os.getcwd()

number = 0
string = ""

for root, dirs, files in os.walk(folder):
    for file in files:
        pathname = os.path.join(root,file)
##        print (pathname)
##        print (os.path.getsize(pathname)/1024/1024)
        if number < os.path.getsize(pathname):
            number = os.path.getsize(pathname)
            string = pathname

print(string)
print()
print(number)
print("Number in bytes")
