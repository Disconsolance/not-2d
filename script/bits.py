import random
import io
import os
from PIL import Image, ImageDraw, ImageSequence, ImageFont
from script.config import *
from script.skews import skews

def ConfigCheck(img):
    w,h = img.size
    Fatal=False
    if STRINGMIN > STRINGMAX:
        print("STRINGMIN is higher than STRINGMAX")
        Fatal=True
    if IMG.endswith(".gif") == False:
        print("Attempted to pass a non-gif")
        Fatal=True
    if STEPDOWN+LINES*(FONTSIZE/FONTSIZEFACTOR)+(LINES-1)*(int(LINESTEP/LINESTEPFACTOR)) > h: # Calculate total height of text
        print("Not all lines fit or do not fit fully.")
    if os.path.isdir("out") == False:
        print("Created an \"out\" folder")
        os.mkdir("out") 
    if Fatal == True:
        exit(1)
    




def AddText(path):
    FONT = ImageFont.truetype(f"script/files/{FONTFILE}", FONTSIZE, encoding="unic")
    frames = []
    im = Image.open(f"in/{path}")
    ConfigCheck(im)
    for frame in ImageSequence.Iterator(im):
        sr=STEPRIGHT
        sd=STEPDOWN

        d = ImageDraw.Draw(frame)

        #i = 0
        #while i < LINES:
            # len = random.randrange(STRINGMIN,STRINGMAX)

            # if GenPointer:
            #     StagedText = GenerateRandomPointer(len)
            # else:
            #     StagedText = GenerateRandomString(len)
            
            # if DrawShadow:
            #     d.text((sr-2,sd+2), StagedText, 'black', FONT)
            # d.text((sr,sd), StagedText, 'white', FONT)
            # sd+=LINESTEP
            # i+=1
        P = skews.Pointer(14, 20, 20)
        ST = skews.RandomString(47, 88, 140)
        P.Draw(d)
        ST.Draw(d)
        
        del d
        b = io.BytesIO()
        frame.save(b, format="GIF")
        frame = Image.open(b)
        frames.append(frame)
    frames[0].save(f'out/42bits-{IMG}', save_all=True, append_images=frames[1:])