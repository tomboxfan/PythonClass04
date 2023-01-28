import turtle

turtle.speed(0)


# solution 1

'''
for i in range(11):

    turtle.circle(i * 10)

turtle.done()
'''


# solution 2

for i in range(10):

    turtle.circle((i + 1) * 10)

turtle.done()

'''
as looping variable i's value is : 0, 1, 2, ....9
expression (i+1)'s value is      : 1, 2, 3, ....10
'''
