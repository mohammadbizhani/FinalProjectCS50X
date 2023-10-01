# importing libraries 
import turtle
import time
import random
from sys import exit

# Recieve from the user lenght of the snake
lenght = int(turtle.numinput("snake lenght",
                          "Select the lenght of the snake",
                          default=25,
                          minval=2,
                          maxval=50
                          ))

# our main bool
game_active = True

# Speed
delay = 0.1

# Score
score = 0
high_score = 0
segments = [[290,290]]

# Set up the screen
wn = turtle.Screen()

wn.title("Snake Game by Mohammad")
wn.bgcolor('white')
wn.setup(width=620, height=700)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(290,290)
head.direction = "stop"

# Lists that we need
segments_new = []
default_segments = segments_new

# Snake body
def snakebody():
    for segment in segments:
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("black")
        segment.penup()
        segments_new.append(segment)

while len(segments_new) < lenght:
    snakebody()

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

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
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while game_active == True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1.5)
        head.goto(290,290)
        head.direction = "stop"
        
        # Reset the segments list
        while len(segments_new) < lenght:
            snakebody()
        
        for segment in segments_new:
            segment.reset()
            segment.penup()
        
        # Reset the score
        score = 0

        # Reset the first food
        food.goto(0,0)

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        segments_new.pop().hideturtle()
        
        # For the last food
        if len(segments_new) == 0:
            msg = turtle.Turtle()
            msg.speed(0)
            msg.shape("square")
            msg.color("green")
            msg.penup()
            msg.hideturtle()
            msg.goto(0, 0)
            msg.write("You did it! welldone!", align="center", font=("Courier", 36, "bold"))
            game_active = False
            time.sleep(2)
            turtle.bye()
            exit()
            
        # Move the food to a random spot
        if len(segments_new) > 0:
            x = random.randrange(-290, 290, 20)
            y = random.randrange(-290, 290, 20)
            food.goto(x,y)

        # Shorten the delay
        delay -= 0.0025

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments_new)-1, 0, -1):
        x = segments_new[index-1].xcor()
        y = segments_new[index-1].ycor()
        segments_new[index].goto(x,y)

    # Move segment 0 to where the head is
    if len(segments_new) > 0:
        x = head.xcor()
        y = head.ycor()
        segments_new[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments_new:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(290,290)
            head.direction = "stop"
            
            # Reset the segments list
            while len(segments_new) < lenght:
                snakebody()
        
            for segment in segments_new:
                segment.reset()
                segment.penup()

            # Reset the score
            score = 0
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
