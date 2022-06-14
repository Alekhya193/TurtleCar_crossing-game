from turtle import Turtle
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"level: {self.score}",align="center",font=FONT)

    def level(self):
        self.score+=1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER ",align="center",font=FONT)




