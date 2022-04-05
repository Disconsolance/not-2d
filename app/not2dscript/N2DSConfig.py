# This is not the file to make a not2dscript
# not2dscript files are located in ./scripts/
# This file governs not2dscript parsing and execution, including Orders

# 0 - FRAME
# 1 - TYPE 
# 2 - X pos
# 3 - Y pos 
# 4 - FONTSIZE
# 5 - FONT 
# 6 - DRAWSHADOW 
# 7 - MINLEN 
# 8 - MAXLEN 
# 9 - STRING

# Changeable variables
CanBeRandom=[1,2,3,4,6,7,8] # Which variables in order list can be set to RANDOM
CanBeDefault=[5,6,9] # Which variables in order list can be set to DEFAULT
TYPELIST=["POINTER", "RSTRING"] # Skew names
MAXFONTSIZE=60
MAXRANDMAXLEN = 16 # Max length that rand can get (Will never go above 16)
MINRANDMAXLEN = 5 # Minimum amount that rand can get for MAX
MAXRANDMINLEN = 4
MINRANDMINLEN = 1


# Fluid variables (program sets these themselves)
w=0
h=0