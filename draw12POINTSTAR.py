# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'star' be the variable that manipulates the turtle pen
star = turtle.Pen() 

# \*********************************************************\

# Define functions

def point():
    star.pencolor("red")
    star.backward(15)
    star.forward(50)
    star.left(85)
    star.forward(80)
    star.left(140)
    star.forward(53)
    star.backward(53)
    star.right(140)
    star.backward(80)
    star.right(265)
    star.forward(50)
    star.right(150)

# \*********************************************************\

# \****************** Draw 12 POINT STAR *******************\

# INITIALIZE
star.pencolor("white")
star.left(90)
star.forward(20)
star.right(75)

# LOOP POINTS
for i in range(12):
    point()

# \************************ End ****************************\

# \*********************************************************\
