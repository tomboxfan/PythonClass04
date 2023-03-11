import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

turtle.bgcolor('black')

for x in range(360):

    turtle.pencolor(colors[x % 6])
    '''
    when x          is 0 to 359
    x % 6           is 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5...
    colors[x % 6]   is 'red', 'purple', 'blue', 'green', 'orange', 'yellow', 'red', 'purple', 'blue', 'green', 'orange', 'yellow', 'red', 'purple', 'blue', 'green', 'orange', 'yellow'...
    '''

    turtle.pensize(x / 100 + 1)

    turtle.forward(x)

    turtle.left(59)