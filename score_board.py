from turtle import Turtle
align="center"
font=("courier",24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align=align,font=font)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=align,font=font)
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=align,font=font)

