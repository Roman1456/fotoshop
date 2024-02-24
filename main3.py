from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageFont

im = Image.open("sistem/img3.png")
im = im.filter(ImageFilter.UnsharpMask(radius=2,percent=150,threshold=3))
I1 = ImageDraw.Draw(im)
myfont = ImageFont.truetype('Christmas ScriptC.ttf',100)
I1.text( (28,36) ," Pear",font=myfont,fill=(255,0,0))

im.save("sistem1/img_4.png")