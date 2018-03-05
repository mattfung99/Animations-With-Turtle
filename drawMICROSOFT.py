# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'mic' be the variable that manipulates the turtle pen
mic = turtle.Pen() 

# \*********************************************************\

# Define Variables

wn = turtle.Screen()
wn.colormode(255)

# \*********************************************************\

# \*********************************************************\

# Define functions

def transbefore():
    mic.pencolor("white")
    mic.forward(10)
    mic.right(90)
    mic.forward(10)
    mic.left(90)

def transafter():
    mic.pencolor("white")
    mic.right(90)
    mic.backward(10)
    mic.left(90)
    mic.forward(10)

def square():
    # DRAW SQUARE
    for i in range(4):
        mic.forward(200)
        mic.right(90)

# \*********************************************************\

# \***************** Draw MICROSOFT LOGO *******************\

# INITIALIZE
    mic.left(90)

# YELLOW BOX
transbefore()
mic.pencolor(255, 187, 0)
mic.fillcolor(255, 187, 0)
mic.begin_fill()
square()
mic.end_fill()
transafter()

# GREEN BOX
transbefore()
mic.pencolor(124, 187, 0)
mic.fillcolor(124, 187, 0)
mic.begin_fill()
square()
mic.end_fill()
transafter()

# RED BOX
transbefore()
mic.pencolor(246, 83, 20)
mic.fillcolor(246, 83, 20)
mic.begin_fill()
square()
mic.end_fill()
transafter()

# BLUE BOX
transbefore()
mic.pencolor(0, 161, 241)
mic.fillcolor(0, 161, 241)
mic.begin_fill()
square()
mic.end_fill()
transafter()
mic.backward(10)
mic.left(90)
mic.backward(10)

# \************************ End ****************************\

# \*********************************************************\
