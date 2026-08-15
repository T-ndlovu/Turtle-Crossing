FONT = ("Courier", 18, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.update_scoreboard()  # show initial score

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 10, 'normal'))
