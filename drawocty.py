# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let paint be the variable that manipulates the turtle pen
paint = turtle.Pen()

# \*********************************************************\

# Draw a dank symbol
def draw(): 
    paint.forward(150)
    paint.left(90)
    paint.forward(100)
    paint.left(45)
    paint.forward(100)
    paint.left(90)
    paint.forward(150)
    paint.left(180)

# Loop for drawing the drawing
for i in range(8):
    draw()

# \*********************************************************\