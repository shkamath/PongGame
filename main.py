from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time

screen = Screen()
score = ScoreBoard()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("___________ PONG ____________")
screen.tracer(0)

paddle_l = Paddle((-350,0))
paddle_r = Paddle((350,0))
ball = Ball()

screen.listen()
screen.onkey(paddle_r.up,"o")
screen.onkey(paddle_r.down,"l")
screen.onkey(paddle_l.up,"q")
screen.onkey(paddle_l.down,"a")

game_on = True
sleep_decrement = 0.0
while game_on:
   time.sleep(ball.ball_speed)
   screen.update()
   ball.move()
   if ball.wall_collision():
      ball.bounce_y()
   
   if ball.distance(paddle_r) < 60 and ball.xcor() > 320 or \
      ball.distance(paddle_l) < 60 and ball.xcor() < -320:
      ball.bounce_x()
      sleep_decrement += 0.01
   
   if ball.xcor() > 380:
      score.l_point()
      ball.reset_pos()
   elif ball.xcor() < -380:
      score.r_point()
      ball.reset_pos()




screen.exitonclick()