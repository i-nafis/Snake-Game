from turtle import Turtle
SCORE_CORD = (-200, 280)
FONT = ("arial", 15, "normal")
ALIGN = "Center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt") as data:
                self.highscore = int(data.read())
        except (FileNotFoundError, ValueError):
            self.highscore = 0
            with open("data.txt", "w") as data:
                data.write("0")
        self.color("white")
        self.penup()
        self.goto(SCORE_CORD)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE : {self.score}  HIGH SCORE: {self.highscore}", False, ALIGN, FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def show_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGN, FONT)
        time.sleep(1)
        self.goto(SCORE_CORD)

    def increase(self):
        self.score += 1
        self.update_scoreboard()
