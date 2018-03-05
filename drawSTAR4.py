# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'star' be the variable that manipulates the turtle pen
star = turtle.Pen() 

# \*********************************************************\

# Define functions

def forwardbackwardMiddle():
    star.forward(150)
    star.backward(150)

def forwardbackwardOuter():
    star.forward(180)
    star.backward(180)    

def forwardbackwardInner():
    star.forward(120)
    star.backward(120) 

def drawStarMiddle():
    star.forward(200)
    star.left(198)
    forwardbackwardMiddle()
    star.right(36)
    forwardbackwardMiddle()
    star.left(198)
    star.backward(200)
    star.forward(200)
    star.right(198)
    star.forward(150)
    star.right(72)
    star.forward(150)
    star.right(18)
    star.backward(200)

def drawStarOuter():
    star.forward(240)
    star.left(198)
    forwardbackwardOuter()
    star.right(36)
    forwardbackwardOuter()
    star.left(198)
    star.backward(240)
    star.forward(240)
    star.right(198)
    star.forward(180)
    star.right(72)
    star.forward(180)
    star.right(18)
    star.backward(240)

def drawStarInner():
    star.forward(160)
    star.left(198)
    forwardbackwardInner()
    star.right(36)
    forwardbackwardInner()
    star.left(198)
    star.backward(160)
    star.forward(160)
    star.right(198)
    star.forward(120)
    star.right(72)
    star.forward(120)
    star.right(18)
    star.backward(160)

# \*********************************************************\

# \********************** Draw STAR4 ***********************\

# INITIALIZE
star.left(90)

# LOOP FOR MIDDLE STAR
for i in range(5):
    drawStarMiddle()

# LOOP FOR OUTER STAR
for j in range(5):
    drawStarOuter()

# LOOP FOR INNER STAR
for k in range(5):
    drawStarInner()

# TOUCHUP
forwardbackwardOuter()
forwardbackwardInner()

# \************************ End ****************************\

# \*********************************************************\
