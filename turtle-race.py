import turtle
import time
import random

# setup width and height of screen:
WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")

        # if the string entered is numeric, convert it to integer:
        if racers.isdigit():
            racers = int(racers)
        else:
            # tell user input must be numeric and start over again:
            print("Input is not numeric... Try Again!")
            continue

        # then check if racers entered are btwn 2 and 10:
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2 - 10. Try Again!")

def create_turtle(colors):
    turtles = []
    spacingx = WIDTH / (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        # set pos:
        racer.setpos(-WIDTH / 2 + (i + 1) * spacingx, -HEIGHT / 2 + 20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles

def race(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            dist = random.randrange(1, 20)
            racer.forward(dist)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def init_turtle():
    # initialize the screen:
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)

    # set screen title:
    screen.title("Turtle Racing!")

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)

print("The winner is the turtle with color: ", winner)