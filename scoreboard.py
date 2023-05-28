from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        with open("highscore.txt", "r") as file:
            self.highscore = int(file.read())
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def track_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        if self.score > self.highscore:
            with open("highscore.txt", "w") as file:
                file.write(str(self.score))
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def hide_score(self):
        self.goto(1000, 1000)
        self.clear()




