# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'penta' be the variable that manipulates the turtle pen
penta = turtle.Pen() 

# \*********************************************************\

# Define Variables

wn = turtle.Screen()
wn.colormode(255)

# \*********************************************************\

# \*********************************************************\

# Define functions

def drawpentagon():
    penta.forward(30)
    penta.right(72)    

def drawstar():
    penta.pencolor(244, 66, 128)
    penta.forward(130)
    penta.right(144)
    penta.forward(80)
    penta.left(72)

# \*********************************************************\

# \******************** Draw PENTA STAR ********************\

# INITIALIZE
penta.pencolor("white")
penta.left(36)
penta.forward(15)
penta.right(108)

# LOOP FOR PENTAGON
penta.pencolor(216, 148, 71)
for i in range(5):
    drawpentagon()
    penta.forward(80)
    penta.backward(80)

# TRANSITION
penta.left(72)
penta.forward(50)
penta.right(72)

# LOOP FOR STAR
for j in range(5):
    drawstar()

# \************************ End ****************************\

# \*********************************************************\
