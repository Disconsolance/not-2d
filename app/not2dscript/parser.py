# Parser template
# FRAME:TYPE:FONTSIZE:X:Y:FONT:DRAWSHADOW:MINLEN:MAXLEN:STRING
# For example: 1:POINTER:40:20:20:DOS:1:3:8:DEFAULT
# Would be: Pointer(40,20,20,"DOS",True,3,8,meta.HEX) and be drawn on frame 1


import string
from app.misc import Exceptions
from app.not2dscript import Executor, Order


def Validate(list):
    print("dududud")

def Parse(str):
    tmp = str.split(':', 10)
    if len(tmp) != 10:
        raise Exceptions.NOT2DScriptMisconfig(str)
    return tmp

def InitList(path):
    i=0
    Frames=[]
    FrameBlock=[]

    with open(path) as n2ds:
        for line in n2ds:
            j = Order.Order(Parse(line))
            j.Validate()
            # Consume the TNO chalice
            
            # Check if next frame
            if j.FRAME == i+1:
                Frames.append(FrameBlock) # Append to queue for last frame
                FrameBlock=[] # Clear queue
                i+=1

            # If current frame
            if j.FRAME == i:
                obj = Executor.GetSkew(j) # Get object
                FrameBlock.append(obj)

            else:
                raise Exceptions.NOT2DScriptMisconfig(1, f"Expected {i} or {i+1}, given {j.FRAME}")
    return Frames


                

