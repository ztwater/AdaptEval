# original image
img = Image.open('test.png')
# converted to have an alpha layer
im2 = img.convert('RGBA')
# rotated image
rot = im2.rotate(22.2, expand=1)
# a white image same size as rotated image
fff = Image.new('RGBA', rot.size, (255,)*4)
# create a composite image using the alpha layer of rot as a mask
out = Image.composite(rot, fff, rot)
# save your work (converting back to mode='1' or whatever..)
out.convert(img.mode).save('test2.bmp')
