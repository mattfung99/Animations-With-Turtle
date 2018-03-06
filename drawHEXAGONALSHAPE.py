# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'hex' be the variable that manipulates the turtle pen
hex = turtle.Pen() 

# \*********************************************************\

# Define functions

def drawhex():
    hex.pencolor("black")
    hex.backward(20)
    hex.left(60)
    hex.begin_fill()
    hex.forward(160)
    hex.right(90)
    hex.forward(115)
    hex.right(60)
    hex.forward(106)
    hex.right(152.5)
    hex.forward(40)
    hex.right(27.5)
    hex.forward(60)
    hex.left(60)
    hex.forward(85.5)
    hex.left(90)
    hex.forward(132)
    hex.end_fill()
    hex.left(120)

    # CALIBRATE
    hex.pencolor("white")
    hex.forward(12)
    hex.left(60)
    hex.forward(93.5)
    hex.right(180)

# \*********************************************************\

# \***************** Draw HEXAGONAL SHAPE ******************\

# INITIALIZE
hex.pencolor("white")
hex.backward(55)

for i in range(3):
    drawhex()

# \************************ End ****************************\

# \*********************************************************\
