from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",20,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,275)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        # self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        # self.goto(0, -20)
        # self.write(f"Press Any Key to Restart Game", align=ALIGNMENT, font=FONT)


