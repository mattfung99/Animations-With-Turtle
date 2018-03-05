# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'dav' be the variable that manipulates the turtle pen
dav = turtle.Pen() 

# \*********************************************************\

# Define functions

def calibrate():
    dav.forward(37.5)
    dav.left(60)

def hexagon():
    dav.forward(75)
    dav.left(60)

def triangle():
    dav.forward(75)
    dav.right(120)
    hexagon()

# \*********************************************************\

# \****************** Draw STAR OF DAVID *******************\

# INITIALIZE     
calibrate()

# LOOP FOR HEXAGON
for i in range(6):
    hexagon()
calibrate()

# TRANSITION
dav.right(60)
dav.forward(37.5)
dav.right(120)

# LOOP FOR TRIANGLES
for j in range(6):
    triangle()

# \************************ End ****************************\

# \*********************************************************\
