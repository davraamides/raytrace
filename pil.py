from PIL import Image

im = Image.new('RGB', (1024, 1024))
pix = im.load()
for x in range(128):
    for y in range(128):
        pix[x, y] = (255,0,0)
im.show()