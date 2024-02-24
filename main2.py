from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter

im = Image.open("sistem/img2.png")
im = im.filter(ImageFilter.DETAIL)
I1 = ImageDraw.Draw(im)
I1.text( (28,36) ,"star Wars",fill=(255,0,0))
im.show()
im.save("sistem/img_3.png")