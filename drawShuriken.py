# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'shu' be the variable that manipulates the turtle pen
shu = turtle.Pen() 

# \*********************************************************\

# Define functions

def forwardbackward():
    shu.forward(150)
    shu.backward(150)

def drawShuriken():
    shu.forward(240)
    shu.left(198)
    forwardbackward()
    shu.right(36) 
    forwardbackward()
    shu.left(198)
    shu.backward(240)
    shu.forward(240)
    shu.right(198)
    shu.forward(150)
    shu.right(54)
    shu.forward(150)
    shu.right(18)
    shu.backward(240)

def leftforward():
    shu.left(90)
    shu.forward(40)

# \*********************************************************\

# \******************** Draw xxxx LOGO *********************\

# INITIALIZE
shu.left(90)

# LOOP for drawing Shuriken
for i in range(4):
    drawShuriken()
shu.forward(52.5)

shu.right(90)
shu.forward(20)
shu.left(90)
shu.forward(20)
for j in range(4):
    leftforward()


# \************************ End ****************************\

# \*********************************************************\
