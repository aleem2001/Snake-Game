from turtle import Turtle

#Constants
INITIAL_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    #Initializing snake list and creating snake
    def __init__(self):
        self.my_snake = []
        self.create_snake()
        #Creating a variable to access the head of the snake, i.e the first segment/piece of the snake
        self.head = self.my_snake[0]
        
        #Accessing the last element of the list using index -1 i.e the Tail
        self.tail = self.my_snake[-1]
    
    #The methods create_snake and add_segment Create Snake instances and append them to snake list    
    def create_snake(self):    
        for pos in INITIAL_POSITIONS:
            self.add_segment(pos)
            
    def add_segment(self,position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.my_snake.append(new_snake)
        
    #Adds a new segment to the tail of the snake to extend its length        
    def extend(self):
        #Adding a new segment to the position of the tail of the snake
        self.add_segment(self.tail.position())
        
            
    #Moving the Snake Function
    #for segments in range(start = len(my_snake) - 1, stop = 0, step = -1):
    #The above comment is for understanding as the range function does not take keyword arguments like start, stop or step
    #The following for loop moves our snake forward by assigning the coordinates of the piece/segment ahead of it to itself, and in the end the first piece/segment is moved forward, after the pieces/segments behind it have taken the position of the piece/segment directly ahead of it
    #In short, the tail follows the head
    def move(self):
        for segment_no in range(len(self.my_snake) - 1, 0, -1):
            new_x = self.my_snake[segment_no - 1].xcor()
            new_y = self.my_snake[segment_no - 1].ycor()
            self.my_snake[segment_no].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    #The following methods are for moving the Snake up, down, left & right
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
    #resetting the snake's position
    def reset(self):
        #moving the dead snake segments to a place beyond the screen
        for segment in self.my_snake:
            segment.goto(1000,1000)
        #clears the my_snake list
        self.my_snake.clear()
        #creating a new snake
        self.create_snake()
        self.head = self.my_snake[0]
        self.tail = self.my_snake[-1]