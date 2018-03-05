# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'ya' be the variable that manipulates the turtle pen
ya = turtle.Pen() 

# \*********************************************************\

# Define functions

def forwardleft():
    ya.forward(60)
    ya.left(90)

def forwardright():
    ya.forward(60)
    ya.right(90)    

def lines():
    ya.forward(90)
    ya.backward(180)
    forwardleft()

def box():
    forwardright()
    forwardleft()
    ya.backward(60)
    ya.right(90)

def reverse():
    ya.left(90)
    forwardright()
    ya.backward(60)
    ya.left(90)
    ya.backward(60)
    
# \*********************************************************\

# \********************** Draw 亞 yà ***********************\

# DRAW TOP LINE
lines()

# TRANSITION 1
ya.backward(60)

# DRAW BOXES
for i in range(4):
    box()

# REACH BOTTOM
for j in range(2):
    reverse()

# TRANSITION 2
ya.forward(60)
ya.left(90)
ya.backward(30)

# DRAW BOTTOM LINE
lines()

# \************************ End ****************************\

# \*********************************************************\
