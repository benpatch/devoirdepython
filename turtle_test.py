__author__ = 'tchilabalo'

import turtle

turtle.forward(88)
turtle.left(90)
turtle.forward(88)
turtle.left(120)
turtle.forward(170)

turtle.penup()
turtle.setpos(0, 0)
turtle.pendown()

turtle.left(190)
i=0
while (i < 4):
    turtle.forward(50)
    turtle.left(90)
    i=i+1

turtle.done()