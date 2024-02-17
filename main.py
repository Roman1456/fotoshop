from PIL import Image
from PIL import ImageDraw

im = Image.open("sistem/img.png")
I1 = ImageDraw.Draw(im)
I1.text( (28,36) ,"nice car",fill=(255,0,0))
im.show()
im.save("car2.png")