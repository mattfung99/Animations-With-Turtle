# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'dav' be the variable that manipulates the turtle pen
dav = turtle.Pen() 

# \*********************************************************\

# Define functions

def forwardleft():
    dav.forward(125)
    dav.left(120)

def turn():
    dav.left(120)
    dav.forward(25)
    dav.left(60)

def drawSOD():
    forwardleft()
    dav.forward(75)
    turn()
    dav.forward(25)
    dav.right(120)
    dav.forward(100)
    turn()
    forwardleft()
    dav.forward(75)
    dav.right(60)
    dav.backward(50)

# \*********************************************************\

# \****************** Draw STAR OF DAVID *******************\

# LOOP for drawing STAR OF DAVID
for i in range(6):
    drawSOD()

# \************************ End ****************************\

# \*********************************************************\
