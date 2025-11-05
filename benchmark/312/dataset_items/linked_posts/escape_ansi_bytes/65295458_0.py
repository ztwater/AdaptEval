ascii_string = 'ls\r\n\x1b[00m\x1b[01;31mexamplefile.zip\x1b[00m\r\n\x1b[01;31m'
decoded_string = ascii_string.encode().decode('ascii')
print(decoded_string) 

>ls
>examplefile.zip
>
