from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.penup()
        self.goto(position)

    def move_forward(self):
        x_coordinate = self.xcor()
        y_coordinate = self.ycor()
        new_y = y_coordinate + 20
        self.goto(x_coordinate, new_y)

    def move_backward(self):
        x_coordinate = self.xcor()
        y_coordinate = self.ycor()
        new_y = y_coordinate - 20
        self.goto(x_coordinate, new_y)
