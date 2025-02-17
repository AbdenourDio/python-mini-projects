import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win thee race? enter a color : ")
is_race_on = False

turtle.colormode(255)

color_list = ["red","green","orange","blue", "purple","yellow"]
y = -100

all_turtles = []
for turtle_index in range(6):
    arthur = Turtle(shape="turtle")
    arthur.penup()
    arthur.goto(x=-230, y=y)
    arthur.color(color_list[turtle_index])
    all_turtles.append(arthur)
    y += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"you have won! {winner} turtle has won the race")
            else:
                print(f"you have lost! {winner} turtle has won the race")


        random_forward = random.randint(0,10)
        turtle.forward(random_forward)







screen.exitonclick()



















