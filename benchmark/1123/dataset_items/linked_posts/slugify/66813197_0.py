> filename = "This is a väryì' Strange File-Nömé.jpeg"
> pattern = re.compile(r'[^-a-zA-Z0-9.]+')
> slugify(filename,regex_pattern=pattern) 
'this-is-a-varyi-strange-file-nome.jpeg'
