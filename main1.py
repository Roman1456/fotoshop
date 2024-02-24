from PIL import Image, ImageFont
from PIL import ImageDraw
from PIL import ImageFilter

im = Image.open("sistem/img1.png")
im = im.filter(ImageFilter.EDGE_ENHANCE)
I1 = ImageDraw.Draw(im)
myfont = ImageFont.truetype('Christmas ScriptC.ttf',100)
I1.text( (28,36) ," Sea",font=myfont,fill=(255,0,0))

im.save("sistem1/img_2_.png")