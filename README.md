# Turtle Race Game

## Description

This is a simple turtle racing game implemented using the Python `turtle` graphics library. It allows the user to bet on which turtle (identified by color) will win the race. Multiple turtles race across the screen, and the first one to reach the finish line is declared the winner.

## How to Play

1.  **Run the script:** Execute the Python script. A window titled "Welcome to the turtle race!" will appear.
2.  **Place your bet:** A text input dialog will prompt you with "Who would win? Enter a color between: \['red', 'green', 'blue', 'orange', 'yellow', 'purple']". Enter the color of the turtle you think will win and press Enter. The input is case-insensitive.
3.  **Watch the race:** Once you've placed your bet, the turtles will start moving randomly across the screen.
4.  **Game Over:** The race ends when one of the turtles reaches the finish line. The program will announce the winning turtle's color and whether you won your bet.
5.  **Close the window:** Click anywhere on the screen to close the game window.

## Functionality

* **Turtle Creation:** Creates multiple turtle objects, each assigned a different color from a predefined list (`red`, `green`, `blue`, `orange`, `yellow`, `purple`).
* **Starting Positions:** Positions each turtle at the left side of the screen with a vertical offset so they start at different heights.
* **User Betting:** Prompts the user to enter the color of the turtle they predict will win.
* **Random Movement:** In each step of the race, each turtle moves forward a random distance between 0 and 10 units.
* **Winner Determination:** The first turtle to reach or cross the x-coordinate of 220 is declared the winner.
* **Bet Outcome:** The program compares the winning turtle's color with the user's bet and announces whether the user won or lost.
* **Game End:** The race stops as soon as a winner is determined.
* **GUI:** Uses the `turtle` module's `Screen` object to create a graphical window for the game and the `textinput` function to get user input.

## Requirements

* Python 3.x (The `turtle` module is typically included with standard Python installations.)

## Installation

No specific installation is required. Save the provided code as a `.py` file (e.g., `turtle_race.py`) and run it using a Python interpreter.

## Code Explanation

* **`colors_list`:** A list containing the colors assigned to the racing turtles.
* **`turtles_list`:** An empty list that will store the created turtle objects.
* **`starting_y`:** A variable to manage the initial vertical position of each turtle, ensuring they don't overlap.
* **`turtle_race_active`:** A boolean flag to control the main game loop, set to `True` when the user makes a valid bet and `False` otherwise.
* **Turtle Creation Loop:** Iterates through the `colors_list`, creating a `Turtle` object for each color, setting its shape to "turtle", color, hiding the drawing line (`penup()`), setting its starting position, and adding it to the `turtles_list`.
* **Screen Setup:** Creates a `Screen` object, sets the title of the window, and defines the screen dimensions.
* **User Bet Input:** Uses `screen.textinput()` to ask the user for their bet (a color). The input is converted to lowercase for easier comparison.
* **Input Validation:** Checks if the user's input is present in the `colors_list`. If not, it cancels the race.
* **Game Loop (`while turtle_race_active`):** Continues as long as the race is active.
* **Turtle Movement Loop:** Iterates through each turtle in the `turtles_list`, making it move forward a random distance.
* **Win Condition:** Checks if a turtle's x-coordinate is greater than or equal to 220 (the finish line). If so, it determines the winner's color and checks if the user's bet matches. It then prints the result and sets `turtle_race_active` to `False` to end the race.
* **Screen Exit:** `screen.exitonclick()` keeps the window open until the user clicks on it.
