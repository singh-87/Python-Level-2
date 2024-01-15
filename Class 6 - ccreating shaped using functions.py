import random
from turtle import *
turtle = Turtle('turtle')
screen = Screen()
turtle.color('cyan')
screen.bgcolor('black')
turtle.pensize(20)
"""def shapes(sides):
    for i in range(0,sides):
        turtle.forward(100)
        turtle.right(360/sides)
#sides = int(input("How many sides you want your shape to have:"))
sides = int(screen.numinput("Shapes","How many sides you want your shape to have:"))
shapes(sides)
#All the shapes
for i in range(4,11):
    shapes(sides=i)"""
def spiral():
    for i in range(0,201):
        turtle.circle(i)
        turtle.right(5)
        turtle.speed(i)
#spiral()
color = ['blue','green','yellow','magenta','red']
def spirograph():
    for i in range(0,201):
        turtle.speed('fastest')
        turtle.pencolor(random.choice(color))
        turtle.circle(100)
        turtle.setheading(turtle.heading()+50)
#spirograph()
direction = [0,90,180,270,360]
def random_walk():
    for i in range(0,101):
        turtle.speed(i)
        turtle.color(random.choice(color))
        turtle.forward(40)
        turtle.setheading(random.choice(direction))
random_walk()









screen.exitonclick()