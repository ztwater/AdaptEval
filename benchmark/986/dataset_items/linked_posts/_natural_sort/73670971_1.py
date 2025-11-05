# Original solution
data.sort(key=natural_sort())

# Select an additional key
image_files.sort(key=natural_sort(lambda x: x.original_filename))
