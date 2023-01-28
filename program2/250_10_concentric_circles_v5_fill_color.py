import random
import turtle

turtle.speed(0)
turtle.colormode(255)

for i in range(10):

    turtle.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.begin_fill()
    turtle.circle((10 - i) * 10)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.pendown()


turtle.done()

