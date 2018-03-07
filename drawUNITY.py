# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'unity' be the variable that manipulates the turtle pen
unity = turtle.Pen() 

# \*********************************************************\

# Define functions

def initialize():
    unity.left(90)

def triangle():
        unity.forward(30)
        unity.right(120)

def arrow():
    # LEFT SIDE OF ARROW
    unity.begin_fill()
    unity.forward(108)
    unity.left(140)
    unity.forward(103)
    unity.right(140)
    unity.forward(37.5)
    unity.right(40)
    unity.forward(127)
    
    # TRANSITION POINT
    unity.right(100)

    # RIGHT SIDE OF ARROW
    unity.forward(127)
    unity.right(40)
    unity.forward(37.5)
    unity.right(140)
    unity.forward(103)
    unity.left(139.5)
    unity.forward(108)
    unity.end_fill()

    # TRANSITION 2
    unity.right(29)
    unity.forward(30)
    unity.right(30)

# \*********************************************************\

# \******************** Draw UNITY LOGO ********************\

# INITIALIZE 
initialize()

# DRAW INNER TRIANGLE
unity.begin_fill()
for i in range(3):
    triangle()
unity.end_fill()

# TRANSITION 1
initialize()

# DRAW ARROWS
for j in range(3):
    arrow()


# \************************ End ****************************\

# \*********************************************************\
