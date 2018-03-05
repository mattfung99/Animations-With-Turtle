# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'gan' be the variable that manipulates the turtle pen
gan = turtle.Pen() 

# \*********************************************************\

# Define Variable

value = 100

# \*********************************************************\

# \*********************************************************\

# Define functions

def variableshrink():
    global value 
    store = value
    value = store * 0.85

def line():
    global value
    gan.forward(value / 2)
    gan.backward(value)
    gan.forward(value / 2)

def variableenlarge():
    global value
    store = value
    value = store * 1.2

# \*********************************************************\

# \********************** Draw 干 gàn **********************\

# INITIALIZE
gan.left(90)
gan.forward(value)
gan.left(90)

# TOP LINE
variableshrink()
line()

# TRANSITION 1
gan.left(90)
gan.forward(value / 2)
gan.left(90)

# MIDDLE LINE
variableenlarge()
line()

 # TRANSITION 2
gan.left(90)
gan.backward(55)

# \************************ End ****************************\

# \*********************************************************\
