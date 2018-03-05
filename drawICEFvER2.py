# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'box' be the variable that manipulates the turtle pen
box = turtle.Pen() 

# \*********************************************************\

# Define functions

def rightforwardlong():
    box.right(135)
    box.forward(70)

def rightforwardshort():
    box.right(45)
    box.forward(70)

def rightforward():
    rightforwardlong()
    rightforwardshort()

# \*********************************************************\

# \******************** Draw ICEF LOGO *********************\

# INITIALIZE
box.left(135)

# LOOP 1
for i in range(4):
    box.forward(70)

    # FIRST MOVES
    rightforward()
    rightforwardlong()

    # TRANSITION 1
    box.backward(70)
    box.right(45)

    # TRANSITION 2
    box.forward(70)

    #LOOP ALL SIDES
    rightforwardshort()
    for j in range(2):
        rightforward()

    # TRANSITION 3
    box.left(90)

    # TRANSITION 4
    box.forward(70)
    box.left(90)

    # TRANSITION 5
    box.forward(70)
    box.right(45)

# \************************ End ****************************\

# \*********************************************************\
