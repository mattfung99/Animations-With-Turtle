# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'mit' be the variable that manipulates the turtle pen
mit = turtle.Pen() 

# \*********************************************************\

# Define functions

def drawdiamond():
    mit.forward(80)
    mit.right(60)
    mit.forward(80)
    mit.right(120)

def loop():
    mit.pencolor("white")
    mit.forward(1)
    mit.pencolor("red")
    mit.fillcolor("red")
    mit.left(30)
    for i in range(2):
        mit.begin_fill()
        drawdiamond()
        mit.end_fill()
    mit.right(30)
    mit.pencolor("white")
    mit.backward(1)
    mit.right(120)

# \*********************************************************\

# \****************** Draw MITSUBISHI LOGO *****************\

# INITIALIZE
mit.left(90)

# DRAW DIAMONDS
for j in range(3):
    loop()
mit.pencolor("red")
mit.forward(30)

# \************************ End ****************************\

# \*********************************************************\
