import turtle

'''
because the radius of the 10 circles are: 10, 20, 30, .... 100
'''



turtle.speed(0)

for i in range(10):

    turtle.circle((i + 1) * 10)

    '''
    each time I draw a circle, the turtle should move downwards 10 pixels
    '''
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()


turtle.done()

