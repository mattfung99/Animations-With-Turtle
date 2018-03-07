# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'tri' be the variable that manipulates the turtle pen
tri = turtle.Pen() 

# \*********************************************************\

# Define functions

def leftforward():
    for j in range(2):
        tri.left(90)
        tri.forward(7.5)
        
def drawglobo():
    tri.begin_fill()
    for k in range(2):
        leftforward()
    tri.end_fill()
    leftforward()
    tri.right(90)

    tri.begin_fill()
    tri.forward(156)
    tri.left(150)
    tri.forward(180)
    tri.right(60)
    tri.forward(15)
    tri.right(120)
    tri.forward(240)
    tri.right(150)
    tri.forward(207)
    tri.right(90)
    tri.forward(15)
    tri.end_fill()
    tri.backward(7.5)
    tri.right(90)
    tri.backward(7.5)
    tri.left(180)

# \*********************************************************\

# \***************** Draw GLOBO 1965 LOGO ******************\

# INITIALIZE
for i in range(4):
    drawglobo()

# \************************ End ****************************\

# \*********************************************************\
