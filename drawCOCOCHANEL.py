# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'coco' be the variable that manipulates the turtle pen
coco = turtle.Pen() 

# \*********************************************************\

# Define functions

def eightypercentcircle():
    # FIRST 60 DEGRESS OF CIRCLE
    for x1 in range (0,60):
        coco.forward(4)
        coco.right(1)
    coco.left(180)
    
    # THE OTHER 300 DEGREES OF CIRCLE
    coco.begin_fill()
    for x2 in range (0,300):
        coco.forward(4)
        coco.left(1)
    coco.left(90)
    coco.forward(80)
    coco.left(90)

    # INNER 80% CIRCLE
    for x3 in range(0,300):
        coco.forward(2.6)
        coco.right(1)
    coco.left(90)
    coco.forward(83.5)
    coco.end_fill()

# \*********************************************************\

# \******************* Draw CHANEL LOGO ********************\

# INITIALIZE
coco.pencolor("white")
coco.left(180)
coco.forward(120)
coco.right(90)
coco.backward(180)
coco.left(90)
coco.pencolor("black")

# FIRST C
eightypercentcircle()

# TRANSITION
coco.pencolor("white")
coco.right(120)
coco.forward(344)
coco.right(90)
coco.forward(420)
coco.pencolor("black")

# SECOND C
eightypercentcircle()

# TOUCHUP
coco.backward(60)
coco.right(90)

# \************************ End ****************************\

# \*********************************************************\
