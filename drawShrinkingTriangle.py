# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'tri' be the variable that manipulates the turtle pen
tri = turtle.Pen() 

# \*********************************************************\

# Define Variable

value = 400

# \*********************************************************\

# \*********************************************************\

# Define functions

def drawtriangle():
    global value
    tri.forward(value)
    tri.right(120)

def variableshrink():
    global value 
    store = value
    value = store * 0.95

def shrink():
    variableshrink()
    tri.forward(value)
    tri.right(120)
    variableshrink()
    drawtriangle()

# \*********************************************************\

# \************* Draw Shrinking Triangle LOGO **************\

# INITIALIZE
tri.forward(200)
tri.backward(400)
tri.left(60)
drawtriangle()

# LOOP
while(value > 10):
    if(value <= 10):
        break
    else:
        shrink()

# \************************ End ****************************\

# \*********************************************************\
