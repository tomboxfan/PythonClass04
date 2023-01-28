import random
import turtle


turtle.speed(0)


'''
the color is represented in the RGB format.
Hence, (0, 255, 0) means green. Similarly, (255, 0, 0) will be red. 
https://www.w3schools.com/colors/colors_picker.asp
'''
turtle.colormode(255)


for i in range(10):

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
    turtle.circle(30)
    turtle.end_fill()

turtle.done()