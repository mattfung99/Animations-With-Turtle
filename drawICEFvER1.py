# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'box' be the variable that manipulates the turtle pen
box = turtle.Pen() 

# \*********************************************************\

# Define functions

def forwardright():
    box.forward(70)
    box.right(90)

def square():
    for l in range(4):
        forwardright()

def slantedsquare(): 
    square()
    # TRANSITION OG
    box.right(135)
    box.forward(70)
    box.left(45)

def outsideforwardleft():
    box.forward(70)
    box.left(45)

def loopoutside():
    for j in range(2):
        outsideforwardleft()
    box.forward(70)

def loopinside():
    box.forward(70)
    box.left(45)
    forwardright()
    box.forward(70)
    box.left(135)

# \*********************************************************\

# \******************** Draw ICEF LOGO *********************\

# INITIALIZE
box.left(135)
square()

# TRANSITION 1
box.left(135)

# LOOP for Basis
for i in range(4):
    slantedsquare()

# TRANSITION 2
box.forward(70)
box.left(90)

# LOOP for outside border animation
for k in range(4):
    loopoutside()
box.left(45)

# LOOP for inside border animation
for m in range(4):
    loopinside()

# \************************ End ****************************\

# \*********************************************************\

