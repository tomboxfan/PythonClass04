import turtle

# set my pen ------------------------

turtle.pencolor("green")
turtle.pensize(10)
turtle.fillcolor("yellow") # 填充色


# start drawing ---------------------


turtle.begin_fill() # Please help me fill the below star

for i in range(9):

    turtle.forward(60)
    turtle.left(140)
    turtle.forward(60)
    turtle.right(100)

turtle.end_fill()  # ok, I am done, you can start filling now.



# finish ---------------------------
turtle.done()
