from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PING PONG")

screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)



def go_up():
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)


def go_down():
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_over = False

while not game_over:
    screen.update()

screen.exitonclick()
