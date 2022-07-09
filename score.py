from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")




class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.get_high_score())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 240)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high-score.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def get_high_score(self):
        with open("high-score.txt", "r") as f:
            high_score = f.read()
            return high_score

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
