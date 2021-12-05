from turtle import Turtle

class Paddle(Turtle):
   def __init__(self,position):
      super().__init__()
      self.shape("square")
      self.color("white")
      self.shapesize(5,1)
      self.speed("fastest")
      self.pu()
      self.goto(position)     
   
   def up(self):
      (x,y) = self.pos()
      if y >= 250:
         pass
      else:
         y += 20
         self.goto(x,y)
   
   def down(self):
      (x,y) = self.pos()
      if y <= -250:
         pass
      else:
         y -= 20
         self.goto(x,y)
