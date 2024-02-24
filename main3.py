from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter

im = Image.open("sistem/img3.png")
im = im.filter(ImageFilter.UnsharpMask(radius=2,percent=150,threshold=3))
I1 = ImageDraw.Draw(im)
I1.text( (28,36) ," Pear",fill=(255,0,0))
im.show()
im.save("sistem/img_4.png")