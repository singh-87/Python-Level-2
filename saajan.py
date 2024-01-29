import random
from turtle import *
turtle = Turtle('turtle')
screen = Screen()
turtle.color('cyan')
screen.bgcolor('black')
turtle.pensize(5)
#color = ['blue','yellow','cyan','purple','red']
"""def shapes(sides):
  for j in range(4,sides+i):
    turtle.pencolor(random.choice(color))
    turtle.forward(100)
    turtle.right(360/i)
for i in range(10,2,-1):
  shapes(sides=i)
screen.exitonclick()"""
"""def spiral():
  for i in range(0,201):
    turtle.pencolor(random.choice(color))
    turtle.circle(i)
    turtle.speed(i)
    turtle.right(5)
spiral()"""
def spirograph():
  for i in range(0,201):
    turtle.speed('fastest')
    turtle.pencolor(random.choice(color))
    turtle.circle(100)
    turtle.setheading(turtle.heading()+i)
#spirograph()
turtle.begin_fill()
for i in range(0,5):
  turtle.forward(100)
  turtle.right(72)
turtle.fillcolor('cyan')
turtle.end_fill()

turtle.end_fill()
