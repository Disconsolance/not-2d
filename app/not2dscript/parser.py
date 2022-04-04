# Parser template
# TYPE:X:Y:FONTSIZE:FONT:DRAWSHADOW:MINLEN:MAXLEN:STRING
# For example: 1:POINTER:20:20:40:DOS:TRUE:3:8:DEFAULT
# Would be: Pointer(20,20,40,"DOS.ttf",True,3,8,meta.HEX)


import string
from app.misc import exceptions

def Parse(str):
    tmp = str.split(':', 10)
    if len(tmp) != 10:
        raise exceptions.NOT2DScriptMisconfig(str)
    
    


