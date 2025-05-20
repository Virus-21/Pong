import turtle
import winsound
from pong_logic import Ball, Paddle, check_paddle_collision, check_score

# Turtle Setup
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Game objects
ball = Ball()
paddle_a = Paddle(y=0)
paddle_b = Paddle(y=0)

# Turtle graphics for paddles/ball
paddle_a_t = turtle.Turtle()
paddle_a_t.speed(0)
paddle_a_t.shape("square")
paddle_a_t.color("white")
paddle_a_t.shapesize(stretch_wid=5, stretch_len=1)
paddle_a_t.penup()
paddle_a_t.goto(-350, paddle_a.y)

paddle_b_t = turtle.Turtle()
paddle_b_t.speed(0)
paddle_b_t.shape("square")
paddle_b_t.color("white")
paddle_b_t.shapesize(stretch_wid=5, stretch_len=1)
paddle_b_t.penup()
paddle_b_t.goto(350, paddle_b.y)

ball_t = turtle.Turtle()
ball_t.speed(0)
ball_t.shape("square")
ball_t.color("white")
ball_t.penup()
ball_t.goto(ball.x, ball.y)

# Scoreboard
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Keyboard
def paddle_a_up():
    paddle_a.move_up()
    paddle_a_t.sety(paddle_a.y)

def paddle_a_down():
    paddle_a.move_down()
    paddle_a_t.sety(paddle_a.y)

def paddle_b_up():
    paddle_b.move_up()
    paddle_b_t.sety(paddle_b.y)

def paddle_b_down():
    paddle_b.move_down()
    paddle_b_t.sety(paddle_b.y)

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Game loop
while True:
    wn.update()

    ball.move()
    ball_t.setx(ball.x)
    ball_t.sety(ball.y)

    # Bounce top/bottom
    if ball.y > 290:
        ball.y = 290
        ball.bounce_y()
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.y < -290:
        ball.y = -290
        ball.bounce_y()
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Check paddle collisions
    if check_paddle_collision(ball, paddle_b.y, 350):
        ball.x = 340
        ball.bounce_x()
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if check_paddle_collision(ball, paddle_a.y, -350):
        ball.x = -340
        ball.bounce_x()
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Score update
    scorer = check_score(ball)
    if scorer == "A":
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.reset_position()
        ball_t.goto(ball.x, ball.y)

    if scorer == "B":
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.reset_position()
        ball_t.goto(ball.x, ball.y)
