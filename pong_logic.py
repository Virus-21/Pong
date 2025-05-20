# pong_logic.py

class Ball:
    def __init__(self, x=0, y=0, dx=0.5, dy=0.5):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_position(self):
        self.x, self.y = 0, 0
        self.bounce_x()


class Paddle:
    def __init__(self, y=0):
        self.y = y

    def move_up(self):
        self.y += 20

    def move_down(self):
        self.y -= 20


def check_paddle_collision(ball: Ball, paddle_y: float, paddle_x: float):
    return abs(ball.x - paddle_x) < 10 and paddle_y - 50 < ball.y < paddle_y + 50


def check_score(ball: Ball):
    if ball.x > 390:
        return "A"
    elif ball.x < -390:
        return "B"
    return None
