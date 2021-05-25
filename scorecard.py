from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(-15, 250)
        self.color('white')
        self.penup()

        self.ht()
        self.refresh_score()


    def game_over(self):
        self.goto(0, 0)

        self.write("GAME OVER", ("Verdana", 20, "bold"), align="center")


    def refresh_score(self):
        self.clear()
        self.write(f"Score ={self.score} ", font=("Verdana", 15, "normal"), align="center")
        self.score += 1
