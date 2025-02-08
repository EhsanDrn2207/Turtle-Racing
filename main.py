import turtle
import time
import random


WIDTH, HIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try Again!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not is range 2-10. Try Again!")


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1 )
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos()
        racer.pendown()
        turtle.append(racer)

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HIGHT)
    screen. title("Turtle Racing!")


