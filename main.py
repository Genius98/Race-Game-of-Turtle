from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400) #height & weight of the screen
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ") #pop up one window for input of a string
colors = ["red", "orange", "yellow", "green", "blue", "purple"] #six turtle's colour
y_positions = [-70, -40, -10, 20, 50, 80] #so that six turtle can go to 6 individual position
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup() #bcz we dont want to see the drawing line
    new_turtle.color(colors[turtle_index]) #picking up diff colors
    new_turtle.goto(x=-230, y=y_positions[turtle_index]) # in goto we can put x & y(each of the tutrle's position)
    all_turtles.append(new_turtle) #each new turtle will be appened to all turtle list

if user_bet:
    is_race_on = True #when uiser bet hits then race will start

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230: #once they reach upto xcordinate=230 which is the ending point of the race
            is_race_on = False #once the first round is done & we got the winner then race will stop
            winning_color = turtle.pencolor() #holding the turtle color
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10) #using random module to get hold of a random int between 0&10
        turtle.forward(rand_distance) #for forwarding the move of six turtles

screen.exitonclick() #this will hold the screen until I click on it