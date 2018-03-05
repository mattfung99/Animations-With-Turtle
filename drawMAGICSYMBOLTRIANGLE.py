# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'tri' be the variable that manipulates the turtle pen
tri = turtle.Pen() 

# \*********************************************************\

# Define functions

def draw():
    tri.pencolor("white")
    tri.forward(20)
    tri.left(90)
    tri.backward(10)
    tri.left(90)
    tri.backward(2)
    tri.right(90)
    tri.pencolor("black")
    tri.fillcolor("black")
    tri.begin_fill()
    tri.forward(84)
    tri.left(150)
    tri.forward(40)
    tri.right(60)
    tri.forward(15)
    tri.right(120)
    tri.forward(100)
    tri.right(150)
    tri.forward(136)
    tri.right(90)
    tri.forward(15)
    tri.end_fill()
    tri.pencolor("white")
    tri.forward(21)
    tri.right(90)
    tri.forward(10)
    tri.right(90)

# \*********************************************************\

# \************** Draw Magic Symbols Triangle **************\

# LOOP FOR TRIANGLE
for i in range(4):
    draw()
    tri.right(90)
tri.right(180)
tri.forward(5)

# \************************ End ****************************\

# \*********************************************************\
