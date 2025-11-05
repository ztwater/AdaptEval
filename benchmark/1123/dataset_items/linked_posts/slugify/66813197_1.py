> filename = "This is a väryì' Strange File-Nömé.jpeg"
> pattern = re.compile(r'[^-a-zA-Z0-9.]+')
> slugify(filename,regex_pattern=pattern, lowercase=False) 
'This-is-a-varyi-Strange-File-Nome.jpeg'
