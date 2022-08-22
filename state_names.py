from turtle import Turtle
FONT = ("Courier", 12, "normal")

class States_score(Turtle):
    def __init__(self):
        super(States_score,self).__init__()
        self.correct_guessed_states = []
        self.hideturtle()

    def write_state(self,answer,x,y):
        self.penup()
        self.goto(x=x, y=y)
        self.write(arg=answer,font= FONT,align= "center",)

    def correct_answer(self, answer):
        self.correct_guessed_states.append(answer)

    def amount_correct(self):
        count = len(self.correct_guessed_states)
        return count