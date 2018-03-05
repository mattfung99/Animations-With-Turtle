# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'exo' be the variable that manipulates the turtle pen
exo = turtle.Pen()

# \*********************************************************\

# Define functions
def onetwenty():
    exo.forward(150)
    exo.right(120)

def sixty():
    exo.forward(150)
    exo.right(60)    

# \*********************************************************\

# \******************** Draw EXO logo **********************\

exo.left(60)

# First DIAMOND
for i in range(3):
    onetwenty()
    sixty()
sixty()

# TRANSITION 1
exo.forward(130)
exo.right(60)

# Second DIAMOND
for j in range(2):
    sixty()
    onetwenty()
onetwenty()

# TRANSITION 2
exo.forward(130)
exo.backward(130)
exo.left(60)

# TRANSITION 3
sixty()
exo.forward(130)

# \************************ End ****************************\

# \*********************************************************\