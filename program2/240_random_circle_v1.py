import random
import turtle

for i in range(10):

    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.circle(30)

turtle.done()