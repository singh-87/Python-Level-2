import random
from turtle import *
turtle = Turtle('turtle')
screen = Screen()
screen.setup(600,500)
screen.bgcolor('black')
turtle.color('cyan')
turtle.penup()
turtle.goto(x = -200,y=-250)
turtle.pendown()
turtle.setheading(90)
turtle.pensize(7)
turtle.forward(450)
turtle.penup()
turtle.write('START',('ariel',40,'bold'))
turtle.hideturtle()
game_list = []
y_position = [-150,-90,-30,30,90,150]
color = ['red','purple','orange','cyan','yellow','white']
for i in range(0,6):
    turtle = Turtle('turtle')
    turtle.shapesize(3)
    turtle.goto(x = -250,y = y_position[i])
    turtle.color(color[i])
    game_list.append(turtle)
saajan_choice = screen.textinput('Bet game of race','Saajan choice')
vignesh_choice = screen.textinput('Bet game of race','Vignesh choice')
if saajan_choice and vignesh_choice:
    game = True
while game:
    for i in game_list:
        steps = random.randint(1,32)
        i.forward(steps)
        if i.xcor()>260:
            game = False
            winner = turtle.pencolor()
            if saajan_choice==winner:
                print("Saajan wins")
            elif vignesh_choice==winner:
                print("Vignesh wins")

            else:
                print("Computer wins")



screen.exitonclick()