from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake_segment = []
        self.create_snake()

    def create_snake(self):
        x_cor = 0
        for i in range(0, 3):
            self.snake_segment.append(Turtle("square"))
            self.snake_segment[i].color("white")
            self.snake_segment[i].penup()
            self.snake_segment[i].goto(x_cor, 0)
            x_cor -= 20

    def move(self):
        for i in range(len(self.snake_segment) - 1, 0, -1):
            self.snake_segment[i].goto(self.snake_segment[i - 1].pos())
        self.snake_segment[0].forward(20)

    def right(self):
        if self.snake_segment[0].heading() != 180:
            self.snake_segment[0].setheading(0)

    def left(self):
        if self.snake_segment[0].heading() != 0:
            self.snake_segment[0].setheading(180)

    def up(self):
        if self.snake_segment[0].heading() != 270:
            self.snake_segment[0].setheading(90)

    def down(self):
        if self.snake_segment[0].heading() != 90:
            self.snake_segment[0].setheading(270)

    def snake_size(self):
        self.snake_segment.append(Turtle("square"))
        self.snake_segment[-1].color("white")
        self.snake_segment[-1].penup()

    def reset(self):
        for i in self.snake_segment:
            i.goto(100000,100000)
        self.snake_segment.clear()
        self.create_snake()

