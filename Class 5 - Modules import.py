"""#MODULES/LIBRARY/EXTENSION IN PYTHON
#random,time,turtle,tkinter,ttkbootstrap,matplotlib.pyplot
#each python file is a module
import saajan
saajan.multiply(34,92)
import saajan as jan
jan.multiply(28372,989981)
from saajan import multiply
multiply(283,902)
from saajan import *
multiply(1293920,293310)"""
from turtle import *
turtle = Turtle('turtle')
turtle.color('cyan')
turtle.pensize(5)
screen = Screen()
screen.bgcolor('black')
"""for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)"""
"""for i in range(0,2):
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)"""
"""turtle.begin_fill()
for i in range(0,5):
    turtle.color('purple')
    turtle.forward(100)
    turtle.right(72)
turtle.fillcolor('cyan')
turtle.end_fill()"""
"""for i in range(0,11):
    turtle.forward(5)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()"""
turtle.setheading(270)
turtle.forward(100)
print(turtle.heading())
screen.exitonclick()
