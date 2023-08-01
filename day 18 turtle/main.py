from turtle import Turtle, Screen

alex = Turtle()
alex.shape("turtle")
alex.color("blue")
alex.speed("fastest")

def draw_circle1():
    for _ in range(360):
        alex.forward(1)
        alex.left(1)

for i in range(0,360//10):
    alex.circle(100)
    alex.right(10)

screen = Screen()
screen.exitonclick()
