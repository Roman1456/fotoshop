from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageFont

im = Image.open("sistem/img2.png")
im = im.filter(ImageFilter.DETAIL)
I1 = ImageDraw.Draw(im)
myfont = ImageFont.truetype('Christmas ScriptC.ttf',100)
I1.text( (28,36) ,"star Wars",font=myfont,fill=(255,0,0))

im.save("sistem1/img_3_.png")