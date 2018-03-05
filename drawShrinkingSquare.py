# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'sqr' be the variable that manipulates the turtle pen
sqr = turtle.Pen() 

# \*********************************************************\

# Define Variable

value = 350

# \*********************************************************\

# \*********************************************************\

# Define functions

def threequarterssquare():
    sqr.forward(value)
    sqr.right(90)

def drawsquare():
    global value
    for i in range(2):
        threequarterssquare()

def variableshrink():
    global value 
    store = value
    value = store * 0.95

def shrink():
    variableshrink()
    sqr.forward(value)
    sqr.right(90)
    variableshrink()
    drawsquare()

# \*********************************************************\

# \************* Draw Shrinking Triangle LOGO **************\

# INITIALIZE
sqr.forward(175)
sqr.backward(350)
sqr.left(90)
drawsquare()

# LOOP
while(value > 10):
    if(value <= 10):
        sqr.right(180)
        break
    else:
        shrink()

# \************************ End ****************************\

# \*********************************************************\
