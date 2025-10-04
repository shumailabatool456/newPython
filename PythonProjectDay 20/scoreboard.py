from turtle import Turtle

alignment = "center"
Font = ("Arial", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        try:
            with open("high_score.txt") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=alignment, font=Font)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def increase_powerup_score(self, points=5):
        self.score += points
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


    def game_over(self):
        self.reset()
        self.goto(0, 0)
        self.write("GAME OVER", align=alignment, font=Font)
