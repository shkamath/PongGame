from turtle import Turtle

class ScoreBoard(Turtle):
   def __init__(self):
      super().__init__()
      self.left_player = 0
      self.right_player = 0
      self.color("white")
      self.pu()
      self.hideturtle()
      self.update_score()
      
   def l_point(self):
      self.left_player += 1
      self.update_score()
   
   def r_point(self):
      self.right_player += 1
      self.update_score()

   def update_score(self):
      self.clear()
      self.goto(-100,200)
      self.write(self.left_player, font=("Courier",80,"normal"))
      self.goto(100,200)
      self.write(self.right_player, font=("Courier",80,"normal"))