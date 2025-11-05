s = 'Very / Unsafe / file\nname hähä \n\r .txt'
clean_basename = slugify(os.path.splitext(s)[0])
clean_extension = slugify(os.path.splitext(s)[1][1:])
if clean_extension:
    clean_filename = '{}.{}'.format(clean_basename, clean_extension)
elif clean_basename:
    clean_filename = clean_basename
else:
    clean_filename = 'none' # only unclean characters
