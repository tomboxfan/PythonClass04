import turtle

turtle.goto(0, 0)
turtle.speed(1000000)
turtle.bgcolor('black')

a = 0
b = 0
c = 0
d = 0
e = 0

while a < 380:
    turtle.color('red')
    turtle.right(90)
    turtle.forward(a * 5)
    a = a + 1

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

while b < 500:
    turtle.color('orange')
    turtle.right(90)
    turtle.forward(b * 4)
    b = b + 1

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

while c < 700:
    turtle.color('yellow')
    turtle.right(90)
    turtle.forward(c * 3)
    c = c + 1

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

while d < 1200:
    turtle.color('green')
    turtle.right(90)
    turtle.forward(d * 2)
    d = d + 1

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

while e < 2000:
    turtle.color('blue')
    turtle.right(90)
    turtle.forward(e)
    e = e + 1

turtle.done()