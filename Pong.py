# Pong Game
import turtle
import time

# Screen
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-395, 295)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(780)
    border.rt(90)
    border.fd(580)
    border.rt(90)
    border.fd(780)
    border.rt(90)
    border.fd(580)
    border.rt(90)
border.hideturtle()

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-360, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2q

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    if y > 235:
        y = 235
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    if y < -225:
        y = -225
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    if y > 235:
        y = 235
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    if y < -225:
        y = -225
    paddle_b.sety(y)


# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if paddle_b.ycor() > 249:
        paddle_b.sety(250)

    if paddle_b.ycor() < -251:
        paddle_b.sety(-250)

    if paddle_a.ycor() > 249:
        paddle_a.sety(250)

    if paddle_a.ycor() < -251:
        paddle_a.sety(-250)

    if ball.ycor() > 275:
        ball.sety(275)
        ball.dy *= -1

    if ball.ycor() < -265:
        ball.sety(-265)
        ball.dy *= -1

    if ball.xcor() > 370:
        paddle_b.goto(350, 0)
        paddle_a.goto(-360, 0)
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(0.2)

    if ball.xcor() < -380:
        paddle_b.goto(350, 0)
        paddle_a.goto(-360, 0)
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(0.2)

    # Paddle and ball collisions
    if (329 < ball.xcor() < 350) and (paddle_b.ycor() + 60 > ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(329)
        ball.dx *= -1

    if (-329 > ball.xcor() > -350) and (paddle_a.ycor() + 60 > ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-329)
        ball.dx *= -1

    # # AI Player
    # if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
    #     paddle_b_up()
    #
    # if paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
    #     paddle_b_down()

    if score_a > 9:
        ball.hideturtle()
        pen.goto(0, 0)
        pen.write("Player A wins!", False, align="center", font=("Courier", 36, "normal"))
        time.sleep(1)

    if ball.xcor() < -380 and score_b > 9:
        ball.hideturtle()
        pen.goto(0, 0)
        pen.write("Player B wins!", False, align="center", font=("Courier", 36, "normal"))
        time.sleep(1)
