import random
from PIL import Image, ImageDraw, ImageSequence
from app.not2dscript import Parser, Order
from app.skews import skews,meta
from app.misc import Exceptions
# FRAME:TYPE:X:Y:FONTSIZE:FONT:DRAWSHADOW:MINLEN:MAXLEN:STRING

def SatisfyKeywords():
    pass

def GetSkew(ord : Order.Order):
    if ord.TYPE == "POINTER":
        return skews.Pointer(ord)
    if ord.TYPE == "RSTRING":
        return skews.RandomString(ord)

def Execute(Queue, frame):
    for i in Queue:
        i.Draw(frame)
    return frame





