# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 600
HEIGHT = 600
DELAY = 20


def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY)


# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("My Turtle Game")

screen.tracer(0)
# Create a turtle to do your bidding
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")
# Your turtle awaits your command

move_turtle()

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()
