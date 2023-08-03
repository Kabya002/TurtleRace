import random
from turtle import Turtle, Screen

is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []
for i in range(len(colors)):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_input:
    is_on = True

while is_on:
    for i in all_turtles:
        i.forward(random.randint(0, 10))
        if i.xcor() >= 230:
            winner = i.pencolor()
            if winner == user_input:
                print(f"Congrats! {user_input.capitalize()} has won the race.")
            else:
                print(f"Sorry. {winner.capitalize()} is the winner.")
            is_on = False









screen.exitonclick()