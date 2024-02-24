from PIL import Image
from PIL import ImageDraw
from PIL import ImageEnhance
from PIL import ImageFont

im = Image.open("sistem/img.png")
im = ImageEnhance.Brightness(im).enhance(1.8)
I1 = ImageDraw.Draw(im)
myfont = ImageFont.truetype('Christmas ScriptC.ttf',100)
I1.text( (28,36) ,"nice car",font=myfont, fill=(255,0,0))

im.save("sistem1/img_1_.png")