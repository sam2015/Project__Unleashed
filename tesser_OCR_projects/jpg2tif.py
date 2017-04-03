from PIL import Image

input = 'CAT.jpg'
outtif = 'me2.tif'

im=Image.open(input)
im2=im.convert('1')
im2.save(outtif, 'TIFF')
