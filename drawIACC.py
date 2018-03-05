# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'iacc' be the variable that manipulates the turtle pen
iacc = turtle.Pen() 

# \*********************************************************\

# Define functions

def drawhexagon():
    # LOOP FOR HEXAGON
    for i in range(6):
        iacc.forward(100)
        iacc.right(60)
    iacc.right(60)

def drawhexagontrigger():
    drawhexagon()
    iacc.backward(50)
    
def twohexagon(): 
    for j in range(2):
        drawhexagontrigger()

def rounds():
    drawhexagontrigger()
    drawhexagon()

# \*********************************************************\

# \******************** Draw IACC LOGO *********************\

# INITIALIZE
iacc.left(150)

# LOOP FOR FIRST SET OF HEXAGONS
twohexagon()

# TRANSITION FOR SECOND SET OF HEXAGONS
iacc.backward(50)
iacc.left(120)

# LOOP FOR SECOND SET OF HEXAGONS
rounds()

# \************************ End ****************************\

# \*********************************************************\
