# FRAME:TYPE:X:Y:FONTSIZE:FONT:DRAWSHADOW:MINLEN:MAXLEN:STRING
from app.skews import meta
from app.not2dscript.N2DSConfig import *
from app.misc import Exceptions
from app.config import FONTFILE, DrawShadow
import random

class Order:
    STARTFRAME=0
    ENDFRAME=0
    TYPE=""
    X=0
    Y=0
    FONTSIZE=0
    FONT=""
    DRAWSHADOW=True
    LEN=0
    STRING=""

    def SetVar(self, index, var):
        match index:
            case 0:
                self.STARTFRAME=int(var)
            case 1:
                self.ENDFRAME=int(var)
            case 2:
                self.TYPE=var
            case 3:
                self.X=int(var)
            case 4:
                self.Y=int(var)
            case 5:
                self.FONTSIZE=int(var)
            case 6:
                self.FONT=var
            case 7:
                self.DRAWSHADOW=var
            case 8:
                self.MINLEN=int(var)
            case 9:
                self.MAXLEN=int(var)
            case 10:
                self.STRING=var
            case _:
                Exceptions.NOT2DScriptMisconfig(5)

    def MakeRandom(self, index):
        match index:
            case 2:
                self.SetVar(index, random.choice(TYPELIST))
            case 3:
                self.SetVar(index, random.randrange(0,w))
            case 4:
                self.SetVar(index, random.randrange(0,h))
            case 5:
                self.SetVar(index, random.randrange(1,MAXFONTSIZE))
            case 6:
                self.SetVar(index, bool(random.getrandbits(1)))
            case 8:
                self.SetVar(index, random.randrange(MINRANDMINLEN, MAXRANDMINLEN)) # Cannot be 0
            case 9:
                self.SetVar(index, random.randrange(MINRANDMAXLEN, MAXRANDMAXLEN))

    def MakeDefault(self, index):
        match index:
            case 6:
                self.FONT = FONTFILE
            case 7:
                self.DRAWSHADOW = DrawShadow
            case 10:
                if self.TYPE == "POINTER":
                    self.STRING = meta.HEX
                elif self.TYPE == "RSTRING":
                    self.STRING = meta.GENSTR

    def Validate(self):
        # Horror
        if type(self.STARTFRAME) != type(self.ENDFRAME) != type(self.X) != type(self.Y) != type(self.FONTSIZE) != type(self.LEN) != int:
            raise Exceptions.NOT2DScriptMisconfig(2)
        if type(self.TYPE) != type(self.STRING) != str:
            raise Exceptions.NOT2DScriptMisconfig(2)
        if type(self.DRAWSHADOW) != bool:
            raise Exceptions.NOT2DScriptMisconfig(2)

        if self.MINLEN == self.MAXLEN or self.MINLEN > self.MAXLEN:
            raise Exceptions.NOT2DScriptMisconfig("MINLEN is equal or greater than MAXLEN")

    def __init__(self, list):
        for i in range(len(list)):
            if list[i] == "DEFAULT" and i in CanBeDefault:
                self.MakeDefault(i)
            elif list[i] == "RANDOM" and i in CanBeRandom:
                self.MakeRandom(i)
            else:
                self.SetVar(i, list[i])

