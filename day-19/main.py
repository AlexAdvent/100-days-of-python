from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwars():
    tim.backward(10)
def right():
    tim.right(5)
def left():
    tim.left(5)

screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwars)
screen.onkey(key="a",fun=left)
screen.onkey(key="d",fun=right)
screen.exitonclick()