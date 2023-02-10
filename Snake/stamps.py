# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 600
HEIGHT = 600

snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

move = input("move:L/R/U/D: ")
x = True
while x:
    if move == 'R':
        old_head = snake[-1]
        new_head = [old_head[0] + 20, old_head[1]]
        snake.append(new_head)
        # snake.pop(0)
        print(snake)
        direction = 'R'
    elif move == 'L':
        old_head = snake[-1]
        new_head = [old_head[0] - 20, old_head[1]]
        snake.append(new_head)
        # snake.pop(0)
        print(snake)
        direction = 'L'
    elif move == 'U':
        old_head = snake[-1]
        new_head = [old_head[0], old_head[1]+20]
        snake.append(new_head)
        # snake.pop(0)
        print(snake)
    elif move == 'D':
        old_head = snake[-1]
        new_head = [old_head[0], old_head[1]-20]
        snake.append(new_head)
        # snake.pop(0)
        print(snake)
    else:
        print('wrong move')
        x = False
        break
    move = input("move:L/R/U/D: ")

print(len(snake))
# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("My Turtle Game")

screen.tracer(0)
# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("turtle")
stamper.fillcolor("green")
stamper.shapesize(18 / 20)

for i in range(len(snake)):
    stamper.stamp()
    stamper.penup()
    stamper.goto(tuple(snake[i]))


# Your turtle awaits your command

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()
