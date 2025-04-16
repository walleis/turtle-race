from turtle import Turtle, Screen
import random

# Colors list.
colors_list = ["red", "green", "blue", "orange", "yellow", "purple"]

# Turtles list.
turtles_list = []

# Stores the y coordinate.
starting_y = -150

# Make sure the turtle race don't start before the user makes the bet.
turtle_race_active = False

# for loop responsible for creating the turtles.
for colors in colors_list:
    turtle = Turtle(shape="turtle")
    turtle.color(colors) # Pick a color from the colors_list.
    turtle.penup() # Hide the line.
    turtle.goto(x= -230, y= starting_y) # Set the starting point.
    starting_y += 50 # Increase the y position value to create other turtles above.
    turtles_list.append(turtle) # Stores the turtles at turtle_list.

# GUI elements.
screen = Screen() # Create the screen object.
screen.title("Welcome to the turtle race!") # This is titlebar of the GUI.
screen.setup(width=500, height=400) # Screen resolution.
user_bet = screen.textinput(title="Turtle Race", prompt=f"Who would win? Enter a color between: {colors_list}").lower() # Asks who would win.

# If the user input something, it will start.
if user_bet == colors_list:
    turtle_race_active = True
else:
    print("Invalid input. Cancelling the turtle race.")
    turtle_race_active = False

# while loop responsible for repeating the forward input.
while turtle_race_active:
    # for loop responsible for making individual turtles go forward.
    for turtle in turtles_list:
        random_forward = random.randint(0, 10)
        turtle.forward(random_forward)
        if turtle.xcor() >= 220: # Who wins first will end the turtle race.
            winner_turtle = turtle.pencolor()
            if user_bet == winner_turtle: # If the user wins the bet, they will be welcome with a win output.
                print(f"The {winner_turtle} got it in first place! You've won!")
                turtle_race_active = False
            else: # If the user loses the bet, they will be welcome with a lose output.
                print(f"The {winner_turtle} got it in first place! You've lose!")
                turtle_race_active = False

# Closes on click.
screen.exitonclick()
