import random
import turtle as t

t.bgcolor('yellow') # This adds a yellow background


# Create a caterpillar turtle
caterpillar = t.Turtle() # Create a new turtle for the caterpillar.
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0) # We don’t want the turtle to move before the game starts.
caterpillar.penup()
caterpillar.hideturtle() # This command hides the turtle.


## Create a leaf turtle
leaf = t.Turtle() # This turtle will draw the leaves.
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), \
            (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)


## Add some text
game_started = False
text_turtle = t.Turtle()
# This line draws some text on the screen.
text_turtle.write('Press SPACE to start', align='center', \
                    font=('Arial', 16, 'bold'))
# This hides the turtle
# but not the text
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
# The turtle needs to stay where it
# is, so that it can update the score.
score_turtle.speed(0)


## Placeholder function
def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x,y) = caterpillar.pos()

    outside = x < left_wall or \
              x > right_wall or \
              y < bottom_wall or \
              y > top_wall

    # return the bool of outside
    return outside


def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align='center',
            font=('Arial', 30, 'normal'))


def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    # 50 pixels from the right
    x = (t.window_width() / 2) - 50
    # 50 pixels from the top
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right',
                        font=('Arial', 40, 'bold'))


def place_leaf():
    leaf.ht() # ht is a short for hideturtle
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st() # st is a short fpr showturtle

## Game starter
def start_game():
    global game_started

    """
    If the game has already started, the return
    command makes the function quit so it doesn’t
    run a second time
    """
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear() # Clear the text from the screen.

    caterpillar_speed = 2
    caterpillar_length = 3
    # The turtle stretches into acaterpillar shape.
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)

        """
        The caterpillar eats than 20 pixels away
        the leaf when it’s less
        """
        if caterpillar.distance(leaf) < 20:
            # Add a new leaf as the prevoius leaf has been eaten
            place_leaf()

            # this will make caterpillar grow longer
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed += 1
            score += 10
            display_score(score)

        if outside_window():
            game_over()
            break


def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)


t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.listen()
t.mainloop()
