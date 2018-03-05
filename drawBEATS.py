# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'beats' be the variable that manipulates the turtle pen
beats = turtle.Pen() 

# \*********************************************************\

# Define functions

def red():
    beats.pencolor("red")
    beats.fillcolor("red")

def white():
    beats.pencolor("white")
    beats.fillcolor("white")

def leftforward():
    beats.left(90)
    beats.forward(75)

# \*********************************************************\

# \******************** Draw BEATS LOGO ********************\

# INITIALIZE
white()
beats.left(90)
beats.backward(75)
beats.right(90)

# DRAW OUTSIDE RED CIRCLE
red()
beats.begin_fill()
beats.circle(150)
beats.end_fill()

# DRAW INNER WHITE CIRCLE
leftforward()
beats.right(90)
white()
beats.begin_fill()
beats.circle(75)
beats.end_fill()

# TRANSITION TO WHITE BAR
for i in range(2):
    leftforward()
beats.right(90)
white()

# DRAW WHITE BAR
beats.begin_fill()
beats.forward(150)
beats.right(90)
beats.forward(30)
beats.right(90)
beats.forward(150)
beats.end_fill()

# TRANSITION TO INNER RED CIRCLE
beats.left(90)
beats.forward(45)
beats.right(90)
beats.forward(50)
beats.left(90)

# DRAW INNER RED CIRCLE 
red()
beats.begin_fill()
beats.circle(50)
beats.end_fill()
beats.right(90)

# \************************ End ****************************\

# \*********************************************************\
