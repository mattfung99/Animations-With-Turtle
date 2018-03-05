# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'sqr' be the variable that manipulates the turtle pen
sqr = turtle.Pen() 

# \*********************************************************\

# Define Variable

value = 400

# \*********************************************************\

# \*********************************************************\

# Define functions

def threequarterssquare():
    sqr.forward(value)
    sqr.right(90)

def drawsquare():
    global value
    for i in range(3):
        threequarterssquare()

def variableshrink():
    global value 
    store = value
    value = store * 0.95

def shrink():
    variableshrink()
    sqr.forward(value)
    sqr.right(120)
    variableshrink()
    drawsquare()

# \*********************************************************\

# \******************* Draw MattDesign01 *******************\

# INITIALIZE
sqr.left(60)
drawsquare()

# LOOP
while(value > 10):
    if(value <= 10):
        break
    else:
        shrink()

# \************************ End ****************************\

# \*********************************************************\
