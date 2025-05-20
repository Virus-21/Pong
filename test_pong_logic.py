# test_pong_logic.py

import unittest
from pong_logic import Ball, Paddle, check_paddle_collision, check_score

class TestPongLogic(unittest.TestCase):

    def test_ball_movement(self):
        ball = Ball()
        ball.move()
        self.assertEqual(ball.x, 0.5)
        self.assertEqual(ball.y, 0.5)

    def test_ball_bounce_y(self):
        ball = Ball(dy=1)
        ball.bounce_y()
        self.assertEqual(ball.dy, -1)

    def test_ball_bounce_x(self):
        ball = Ball(dx=1)
        ball.bounce_x()
        self.assertEqual(ball.dx, -1)

    def test_reset_position(self):
        ball = Ball(x=100, y=50, dx=0.5)
        ball.reset_position()
        self.assertEqual((ball.x, ball.y), (0, 0))
        self.assertEqual(ball.dx, -0.5)

    def test_paddle_up_down(self):
        paddle = Paddle(y=0)
        paddle.move_up()
        self.assertEqual(paddle.y, 20)
        paddle.move_down()
        self.assertEqual(paddle.y, 0)

    def test_paddle_collision(self):
        ball = Ball(x=345, y=0)
        self.assertTrue(check_paddle_collision(ball, paddle_y=0, paddle_x=350))
        self.assertFalse(check_paddle_collision(ball, paddle_y=0, paddle_x=370))

    def test_score_conditions(self):
        ball_a = Ball(x=400)
        ball_b = Ball(x=-400)
        self.assertEqual(check_score(ball_a), "A")
        self.assertEqual(check_score(ball_b), "B")
        self.assertIsNone(check_score(Ball(x=0)))

if __name__ == '__main__':
    unittest.main()
