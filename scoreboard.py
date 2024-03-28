from turtle import Turtle, Screen
#Constants
ALIGNMENT = 'center'
FONT = ("Verdana", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()

    #Method to update the score board. i.e print the score on the screen
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    #reset game method and update high score
    def reset(self):
        #updating high_score
        if self.score > self.high_score:
            self.high_score = self.score
        
        #resetting score
        self.score = 0
        
        #updating scoreboard
        self.update_scoreboard()
        
    #Method to increase the score 
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
