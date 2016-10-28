from PIL import Image,ImageFont,ImageFont,ImageDraw
import sys
#sys.setdefaultencoding('utf-8')

#Path of picture
headPath = r"/home/yours/cyw/picture/"

#Path of output
outputPath =  r"/home/yours/cyw/AddNumToPic/"

#Path of font
fontPath = r"/home/yours/cyw/AddNumToPic/"

headFile = "63.jpg"
outFile = "output.jpg"

image = Image.open(headPath+headFile,'r')
draw = ImageDraw.Draw(image)

fontsize = min(image.size) / 4

fontobj = ImageFont.truetype(font=fontPath+"Ubuntu-B.ttf", size=fontsize, index=0, encoding='', filename=None)
draw.text((image.size[0]-fontsize,0), text="5", fill=(255,0,0), font=fontobj, anchor=None)
image.save(outputPath+outFile)

