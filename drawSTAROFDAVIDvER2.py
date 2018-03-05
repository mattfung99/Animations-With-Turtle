# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'dav' be the variable that manipulates the turtle pen
dav = turtle.Pen() 

# \*********************************************************\

# Define functions

def calibrate():
    dav.forward(112.5)
    dav.left(120)

def forwardleft():
    dav.forward(225)
    dav.left(120)

def forwardleft2():
    dav.forward(75)
    dav.left(120)

# \*********************************************************\

# \****************** Draw STAR OF DAVID *******************\

# INITIALIZE
calibrate()

# LOOP FOR FIRST TRIANGLE

for i in range(4):
    forwardleft()

# TRANSITION 
for k in range(2):
    forwardleft2()
    dav.left(180)
dav.right(180)

# LOOP FOR SECOND TRIANGLE
for j in range(3):
     forwardleft()
     
# \************************ End ****************************\

# \*********************************************************\
