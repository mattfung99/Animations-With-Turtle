# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'star' be the variable that manipulates the turtle pen
star = turtle.Pen() 

# \*********************************************************\

# Define Variables

wn = turtle.Screen()
wn.colormode(255)

# \*********************************************************\

# \*********************************************************\

# Define functions

def drawinnersquare():
    star.forward(60)
    star.left(90)

def drawoutersquare():
    star.forward(180)
    star.left(90)

def drawtriangle():
    star.forward(180)
    star.left(120)

def looptriangle():
    star.begin_fill()
    for k in range(3):
        drawtriangle()
    star.end_fill()

# \*********************************************************\

# \******************* Draw 4 POINT STAR *******************\

# INITIALIZE
star.pencolor("white")
star.forward(30)
star.left(90)
star.backward(30)

# DRAW INNER SQUARE
star.pencolor(42, 91, 170)
star.fillcolor(42, 91, 170)
star.begin_fill()
for i in range(4):
    drawinnersquare()
star.end_fill()

# TRANSITION
star.forward(30)
star.right(90)
star.forward(1)
star.pencolor("white")
star.forward(59)
star.left(90)
star.pencolor(42, 91, 170)
star.backward(90)

# DRAW OUTER SQUARE
for j in range(4):
    drawoutersquare()
star.right(60)

# LOOP FOR DRAWING TRIANGLES
for l in range(4):
    looptriangle()
    star.left(60)
    star.forward(180)
    star.left(30)

# \************************ End ****************************\

# \*********************************************************\
