from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        
        #Shape size is usually 20 by 20, by stretching length and width by 0.5, we are halving its dimensions making it 10 by 10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        
        #self.speed('fastest') speeds up the animation so that we do not have to see the food piece being created and then move to its coordinates
        self.speed('fastest')
        
        #Calling refresh method to generate food
        self.refresh()
        
    #Refresh method refreshes the food's location to a new location once it has been eaten by the snake
    def refresh(self):
        #Creating random x,y coordinates for the food
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)