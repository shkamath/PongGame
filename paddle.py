from turtle import Turtle
class Paddle():
   def __init__(self):
      self.paddle = Turtle()
      self.paddle.shape("square")
      self.paddle.color("white")
      self.paddle.shapesize(20,80)
      self.paddle.pu()
      self.paddle.goto(350,0)
