import random
import string
import io
import os
from PIL import Image, ImageDraw, ImageSequence, ImageFont


# Input
IMG = "example.gif" # input gif

# Generation
GenPointer=False # TO generate a random string from POINTERCHARLIST, rather than STRINGCHARLIST
DrawShadow=True
LINES=3 

# Chars
STRINGCHARLIST = "%$!?/.=+-@:&\\" + string.hexdigits #chars, picks random from string
POINTERCHARLIST = string.digits + "ABCDEF"

# Text
STRINGMIN=3 
STRINGMAX=16 #MAX string length

# Font
FONTFILE="dos.ttf"
FONTSIZE=40

# Placement
STEPRIGHT = 15 # How far from the left border to draw text
STEPDOWN = 15 # How far from the top border to draw text
LINESTEP = FONTSIZE # How much pixels to go down for each new line
OFFSET = 2 # How much pixels to offset the shadow (if OFFSET is 2: STEPRIGHT-2, STEPDOWN+2)

# Factor
FONTSIZEFACTOR=1.6 # OPTIONAL: How tall is a large character in pixels in comparison to FONTSIZE .
                   # (e.g. if "8" is 25 pixels tall with a font size of 40: 40/25 = 1.6). 
                   # This is (not neccesarily) needed for config checks.

LINESTEPFACTOR=2.6 # True line step distance (LINESTEP divided by actual distance between lines in pixels)

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


def GenerateRandomString(len):  
    str = ""
    i=0
    while i < len:
        str+=random.choice(STRINGCHARLIST)
        i+=1
    return str

def GenerateRandomPointer(len):
    # Comment the line below to remove 8 character limit on pointers (will look like shit)
    len = random.randrange(STRINGMIN,8)
    str = "0x"
    i = 0
    while i < len:
        str+=random.choice(POINTERCHARLIST)
        i+=1
    return str


def AddText(path):
    FONT = ImageFont.truetype(FONTFILE, FONTSIZE, encoding="unic")
    frames = []
    im = Image.open(f"in/{path}")
    ConfigCheck(im)
    for frame in ImageSequence.Iterator(im):
        sr=STEPRIGHT
        sd=STEPDOWN

        d = ImageDraw.Draw(frame)

        i = 0
        while i < LINES:
            len = random.randrange(STRINGMIN,STRINGMAX)

            if GenPointer:
                StagedText = GenerateRandomPointer(len)
            else:
                StagedText = GenerateRandomString(len)
            
            if DrawShadow:
                d.text((sr-2,sd+2), StagedText, 'black', FONT)
            d.text((sr,sd), StagedText, 'white', FONT)
            sd+=LINESTEP
            i+=1
        
        del d
        b = io.BytesIO()
        frame.save(b, format="GIF")
        frame = Image.open(b)
        frames.append(frame)
    frames[0].save(f'out/42bits-{IMG}', save_all=True, append_images=frames[1:])

AddText(IMG)