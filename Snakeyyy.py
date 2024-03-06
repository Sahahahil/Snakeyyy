import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.bgpic("background.png")
wn.setup(width=1650, height=1050)  # Adjusted the screen size
wn.tracer(0)  # Turns off the screen updates

# Draw black borders
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.hideturtle()
border_pen.goto(-295, 295)
border_pen.pendown()
border_pen.pensize(3)
for _ in range(4):
    border_pen.forward(590)
    border_pen.right(90)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Level selection
level = turtle.numinput("Snake Game", "Choose a level (1 for easy, 2 for medium, 3 for hard):", default=1, minval=1, maxval=3)

# Adjust speed based on the selected level
if level == 1:
    delay = 0.05
elif level == 2:
    delay = 0.1
else:
    delay = 0.05

# Walls
walls = []

# Function to create walls
def create_wall(shape, color, stretch_wid, stretch_len):
    wall = turtle.Turtle()
    wall.speed(0)
    wall.shape(shape)
    wall.color(color)
    wall.penup()

    # Check for overlapping positions with existing walls
    while True:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)

        if not position_overlaps_with_wall(x, y) and not is_position_at_center(x, y):
            break

    wall.goto(x, y)
    wall.shapesize(stretch_wid=stretch_wid, stretch_len=stretch_len)
    walls.append(wall)

def position_overlaps_with_wall(x, y):
    for wall in walls:
        if wall.distance(x, y) < 60:
            return True
    return False

def is_position_at_center(x, y):
    return -50 < x < 50 and -50 < y < 50

# Function to generate a new food position that doesn't overlap with walls
def generate_food_position():
    while True:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        if not position_overlaps_with_wall(x, y):
            if not position_overlap_with_new_walls(x, y):
                return x, y

def position_overlap_with_new_walls(x, y):
    for wall in walls:
        if wall.distance(x, y) < 60:
            return True
    return False

# Function to spawn food at a new location
def spawn_food_at_new_location():
    food_x, food_y = generate_food_position()
    food.goto(food_x, food_y)

# Create walls for levels 2 and 3
if level == 2:
    # Create vertical walls
    for _ in range(10):
        create_wall("square", "dark green", 5, 1)

    # Create horizontal walls
    for _ in range(10):
        create_wall("square", "dark green", 1, 5)

elif level == 3:
    # Create vertical walls
    for _ in range(15):
        create_wall("square", "dark green", 3, 1)

    # Create horizontal walls
    for _ in range(15):
        create_wall("square", "dark green", 1, 3)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)  # Adjust the y-coordinate for the score
pen.write("Score: 0      High Score: 0", align="center", font=("Times New Roman", 24, "bold"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)

def reset_game():
    global score, delay, level
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "Stop"

    for segment in segments:
        segment.goto(1000, 1000)

    # Reset walls
    for wall in walls:
        wall.goto(1000, 1000)
    walls.clear()

    segments.clear()

    score = 0
    delay = 0.1

    update_score()

    # Ask the player to choose a level after collision
    level = turtle.numinput("Snake Game", "Collision! Choose a level (1 for easy, 2 for medium, 3 for hard):", default=1, minval=1, maxval=3)

    # Adjust speed based on the selected level
    if level == 1:
        delay = 0.05
    elif level == 2:
        delay = 0.1
    else:
        delay = 0.05

    # Create walls for levels 2 and 3
    if level == 2:
        # Create vertical walls
        for _ in range(10):
            create_wall("square", "dark green", 5, 1)

        # Create horizontal walls
        for _ in range(10):
            create_wall("square", "dark green", 1, 5)

    elif level == 3:
        # Create vertical walls
        for _ in range(15):
            create_wall("square", "dark green", 3, 1)

        # Create horizontal walls
        for _ in range(15):
            create_wall("square", "dark green", 1, 3)

    # Spawn food at a new location
    spawn_food_at_new_location()

    # Rebind keyboard events
    wn.listen()
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "Right")

def update_score():
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        reset_game()

    if head.distance(food) < 20:
        food_x, food_y = generate_food_position()
        food.goto(food_x, food_y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10

        if score > high_score:
            high_score = score

        update_score()

    for wall in walls:
        if head.distance(wall) < 20:
            reset_game()

    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    time.sleep(delay)
