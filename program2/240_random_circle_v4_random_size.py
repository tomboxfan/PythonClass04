import random
import turtle


turtle.speed(0)


'''
https://www.w3schools.com/colors/colors_picker.asp
'''
turtle.colormode(255)


for i in range(100):

    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.fillcolor(r, g, b)

    turtle.begin_fill()

    radius = random.randint(10, 80)
    turtle.circle(radius)

    turtle.end_fill()

turtle.done()