from turtle import Turtle
VERTICAL_MAX = 250
VERTICAL_MIN = -250
HORIZONTAL_MAX = 350
HORIZONTAL_MIN = -350

class Ball(Turtle):
   def __init__(self):
      super().__init__()
      self.shape("circle")
      self.color("yellow")
      self.pu()
      self.goto(0,0)
      self.x_move = 10
      self.y_move = 10
      self.ball_speed = 0.1
   
   def move(self):
      self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

   def wall_collision(self):
      if self.ycor() >= 250 or self.ycor() <= -250:
         return True
      else:
         return False
   
   def bounce_y(self):
      self.y_move *= -1

   def bounce_x(self):
      self.x_move *= -1
      self.ball_speed *= 0.9

   def reset_pos(self):
      self.goto(0,0)
      self.ball_speed = 0.1
      self.bounce_x()
      
