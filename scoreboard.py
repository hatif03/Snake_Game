from turtle import Turtle

FONT = ("Comic Sans MS", 15, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.display()

    def display(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score }", align="center", font=FONT )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.display()

