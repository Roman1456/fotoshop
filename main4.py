from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter

im = Image.open("sistem/img4.png")
im = im.filter(ImageFilter.CONTOUR)
I1 = ImageDraw.Draw(im)
I1.text( (28,36) ," nature",fill=(255,0,0))
im.show()
im.save("sistem/img_5.png")