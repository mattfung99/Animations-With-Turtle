# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'tri' be the variable that manipulates the turtle pen
tri = turtle.Pen() 

# \*********************************************************\

# Define function
def algorithm():
    tri.forward(90)
    tri.left(120)
    tri.forward(180)

    tri.left(120)
    tri.forward(225)
    tri.left(60)
    tri.forward(45)
    tri.left(120)
    tri.forward(180)
    
    tri.right(120)
    tri.forward(90)
    tri.left(180)


# \*********************************************************\

# \**************** Draw Infinity Triangle *****************\

# INITIALIZE
tri.left(120)

# LOOP
for i in range(3):
    algorithm()

# \************************ End ****************************\

# \*********************************************************\



  
