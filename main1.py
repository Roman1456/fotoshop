from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter

im = Image.open("sistem/img1.png")
im = im.filter(ImageFilter.EDGE_ENHANCE)
I1 = ImageDraw.Draw(im)
I1.text( (28,36) ," Sea",fill=(255,0,0))
im.show()
im.save("sistem/img_2.png")