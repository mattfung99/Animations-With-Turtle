# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'tri' be the variable that manipulates the turtle pen
tri = turtle.Pen() 

# \*********************************************************\

# Define functions

def forwardbackward():
    tri.forward(180)
    tri.backward(180)

def lines1():
    forwardbackward()
    tri.left(120)

def smalltriangle():
    tri.forward(312)
    tri.left(120)

def loopsmalltriangle():
    for j in range(3):
        smalltriangle()

def backwardforward():
    tri.backward(180)
    tri.forward(360)

def lines2():
    backwardforward()
    tri.left(120)
    tri.backward(180)

def bigtriangle():
    tri.forward(624)
    tri.left(120)

def loopbigtriangle():
    for l in range(3):
        bigtriangle()

def lasttriangle():
    tri.forward(624)
    tri.right(120)

def looplasttriangle():
    for m in range(3):
        lasttriangle()

# \*********************************************************\

# \************** Draw VECTOR OPEN STOCK DESIGN *************\

# INITIALIZE
tri.right(90)

# LOOP FOR LINES 1
for i in range(3):    
    lines1() 
tri.forward(180)

# TRANSITION 1 
tri.left(150)

# FUNCTION CALLED TO DRAW SMALL TRIANGLE
loopsmalltriangle()

# TRANSITION 2
tri.left(30)

# LOOP FOR LINES 2
for k in range(3):
    lines2()
tri.backward(180)

# TRANSITION 3
tri.right(30)

# FUNCTION CALLED TO DRAW BIG TRIANGLE
loopbigtriangle()

# TRANSITION 4
tri.left(30)
tri.forward(180)
tri.left(90)
tri.forward(312)
tri.right(120)

# FUNCTION CALLED TO DRAW LAST TRIANGLE
looplasttriangle()

# TRANSITION 5
tri.right(60)
tri.forward(312)
tri.left(90)
tri.forward(180)

# \************************ End ****************************\

# \*********************************************************\
