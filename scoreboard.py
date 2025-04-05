from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")



        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.update_score()
    def update_score(self):
        self.write(f"Score={self.score}", align="center", font=("Arial", 10, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME-OVER", align="center", font=("Arial", 10, "bold"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
    def your_score(self):
        self.goto(0,-25)
        self.color("blue")
        self.write(f"Your Score={self.score}", align="center", font=("Arial", 13, "bold"))





