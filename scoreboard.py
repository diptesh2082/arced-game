from  turtle import  Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_paddle = 0
        self.l_paddle = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(100, 250)
        self.write(self.r_paddle, align="center", font=("Arial", 25, 'normal' ))
        self.goto(-100, 250)
        self.write(self.l_paddle, align= 'center', font=("Arial", 30, "normal"))

    def r_point(self):
        self.r_paddle += 1
        self.update_scoreboard()
    def l_point(self):
        self.l_paddle += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 30, "normal"))
