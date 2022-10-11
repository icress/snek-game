from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.setposition(0, 270)
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = data.read()
        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", False, "center", ("Arial", 20, "normal"))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update()

    def score_increase(self):
        self.score += 1
