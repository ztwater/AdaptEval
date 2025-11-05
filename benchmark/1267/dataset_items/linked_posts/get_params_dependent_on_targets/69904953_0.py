rotate_degrees = -90
img = Image.open(input_file_path)
img2 = img.rotate(rotate_degrees, expand=True)
img2.save(output_file_path)
