import Image

im = Image.open('3dgifs6.gif')
print im.format, im.size, im.mode
im.thumbnail((400, 208))
im.save('thumb.jpg', 'GIF')