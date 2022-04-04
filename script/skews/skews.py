# TODO: At least two fucking skews
from script.skews import meta
import random
from PIL import Image, ImageDraw, ImageSequence, ImageFont

class Pointer():
    DRAWSHADOW=False
    FONTSIZE=0
    LEN = 0
    STRING=""
    X=0
    Y=0

    def __init__(self, FONTSIZE, xpos, ypos, FONT=meta.FONT, DrawShadow=meta.DRAWSHADOW, MINLEN=meta.MINSIZE, MAXLEN=meta.MAXSIZE, STRING=meta.HEX):
        self.FONTSIZE=FONTSIZE
        self.FONT = ImageFont.truetype(f"script/files/{FONT}", FONTSIZE, encoding="unic")
        self.DRAWSHADOW = DrawShadow
        self.X = xpos
        self.Y = ypos
        self.LEN = random.randrange(MINLEN, MAXLEN)
        self.STRING = STRING
    
    def GenerateRandomPointer(self):
        # Replace (1,8) with (self.MINLEN,self.MAXLEN) to remove the limit on pointer size
        len = random.randrange(1,8)
        str = "0x"
        i = 0
        while i < len:
            str+=random.choice(self.STRING)
            i+=1
        return str

    def Draw(self, frame):
        StagedText = self.GenerateRandomPointer()

        if meta.DRAWSHADOW:
            frame.text((self.X-2,self.Y+2), StagedText, 'black', self.FONT)
        frame.text((self.X,self.Y), StagedText, 'white', self.FONT)

        return frame
    
class RandomString():
    DRAWSHADOW=False
    FONTSIZE=0
    LEN = 0
    STRING=""
    X=0
    Y=0

    def __init__(self, FONTSIZE, xpos, ypos, FONT=meta.FONT, DrawShadow=meta.DRAWSHADOW, MINLEN=meta.MINSIZE, MAXLEN=meta.MAXSIZE, STRING=meta.GENSTR):
        self.FONTSIZE=FONTSIZE
        self.FONT = ImageFont.truetype(f"script/files/{FONT}", FONTSIZE, encoding="unic")
        self.DRAWSHADOW = DrawShadow
        self.X = xpos
        self.Y = ypos
        self.LEN = random.randrange(MINLEN, MAXLEN)
        self.STRING = STRING
    
    def GenerateRandomPointer(self):
        str = ""
        i=0
        while i < self.LEN:
            str+=random.choice(self.STRING)
            i+=1
        return str

    def Draw(self, frame):
        StagedText = self.GenerateRandomPointer()

        if meta.DRAWSHADOW:
            frame.text((self.X-2,self.Y+2), StagedText, 'black', self.FONT)
        frame.text((self.X,self.Y), StagedText, 'white', self.FONT)

        return frame
