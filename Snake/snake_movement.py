# Import the Turtle Graphics module
import turtle
import random

# Constants
WIDTH = 500
HEIGHT = 500
DELAY = 200
FOOD_SIZE = 10
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"


def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"


def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


# Distance between 2 points
def calculate_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5


# Generate random food
def generate_food():
    x = random.randint(int(- WIDTH / 2 + FOOD_SIZE), int(WIDTH / 2 - FOOD_SIZE))
    y = random.randint(int(- HEIGHT / 2 + FOOD_SIZE), int(HEIGHT / 2 - FOOD_SIZE))
    return x, y


def food_collision():
    global food_pos
    global score
    if calculate_distance(snake[-1], food_pos) < 15:
        food_pos = generate_food()
        food.goto(food_pos)
        score += 1
        return True
    return False

def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collision with margins
    if new_head in snake or new_head[0] < -WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    else:
        snake.append(new_head)

        # Check food collision
        if not food_collision():
            snake.pop(0)

        for item in snake:
            stamper.goto(item[0], item[1])
            stamper.stamp()
        screen.title(f"Sname Game. Score: {score}")
        screen.update()
        turtle.ontimer(game_loop, DELAY)


def reset():
    global score, snake, snake_direction, food_pos
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

    score = 0

    snake_direction = "up"
    food_pos = generate_food()
    food.goto(food_pos)
    game_loop()


# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("My Snake Game")
screen.tracer(0)

# event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(reset, "space")

# Create te snake
stamper = turtle.Turtle()
stamper.shape("square")
stamper.fillcolor("green")
stamper.shapesize(19 / 20)
stamper.penup()

# Create the food
food = turtle.Turtle()
food.shape("circle")
food.fillcolor("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

reset()
# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()

# reset to ask if we want to continue
