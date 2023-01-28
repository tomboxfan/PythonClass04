import turtle

'''
looping variable i's value : 0, 1, 2, .....9
(i + 1)'s value            : 1, 2, 3, .....10
(i + 1) * 10's value       : 10, 20, 30, .....100

I want to find such an expression, its value are: 100, 90, 80,.... 10

-i's value                 : 0, -1, -2 .... -9
(10 - i) value             : 10, 9, 8, .....1
(10 - i) * 10 value        : 100, 90, 80, .... 10


'''



# turtle.speed(0)

for i in range(10):

    # turtle.circle((i + 1) * 10) # draw from small to big
    turtle.circle((10 - i) * 10)  # draw from big to small

    '''
    each time I draw a circle, the turtle should move downwards 10 pixels
    '''
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.pendown()


turtle.done()

