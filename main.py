from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Creating the Screen and defining its properties
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

#screen.tracer(0) does not update the animations/pixels
screen.tracer(0)
#to refresh the animations, we will use screen.update()

#Creating our snake
snake = Snake()

#Creating food
food = Food()

#Creating scoreboard
scoreboard = Scoreboard()

#Listening for the Arrow Key Presses to move the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    #graphics are refreshed using screen.update() after a delay of 0.1 seconds
    screen.update()
    time.sleep(0.1)
    
    #Calling the snake move function
    snake.move()
    
    #Detecting snake's collision with food and updating the score
    if snake.head.distance(food) < 15:
        #refreshing food's coordinates
        food.refresh()
        
        #extending the length of the snake
        snake.extend()
        
        #updating scoreboard
        scoreboard.increase_score()
        
    #Detecting snake's collision with the wall, creating a boundary range of -290<x<290 and -290<y<290
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:  
        game_is_on = False
        scoreboard.game_over()
        
    #Detecting snake's head collision with any segment of the tail, i.e any part of its body, we used list slicing
    for segment in snake.my_snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
        
        
#Does not allow the screen to vanish until it is clicked
screen.exitonclick()