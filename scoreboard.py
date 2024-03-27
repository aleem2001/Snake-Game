from turtle import Turtle, Screen
#Constants
ALIGNMENT = 'center'
FONT = ("Verdana", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()

    #Method to update the score board. i.e print the score on the screen
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
  
    #Method to increase the score 
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    #Game over method
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        