import turtle

# set the pen ----------------------------------

turtle.pencolor("red") # set pen color
turtle.pensize(10)     # set pen size

# start drawing --------------------------------

for i in range(3):

    turtle.forward(200) # let the turtle draw a straight line, with length = 200 pixels
    turtle.left(120)    # let the turtle turn left 120 degree

turtle.done()