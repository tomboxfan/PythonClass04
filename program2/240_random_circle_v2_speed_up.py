import random
import turtle



'''
'fastest' : 0
'fast'    : 10
'normal'  : 6
'slow'    : 3
'slowest' : 1
'''

turtle.speed(0)



for i in range(10):

    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.circle(30)

turtle.done()