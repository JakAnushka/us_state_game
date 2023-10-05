import pandas
import turtle


class state:
    def __init__(self):
        self.read_file()
        self.score=0

    def read_file(self):
        self.data=pandas.read_csv("50_states.csv")
        self.name_state=self.data["state"].to_list()

    def check_answer(self,user_answer):
        for correct_answer in self.name_state:
            if correct_answer==user_answer:
                self.score+=1
            else:
                self.dict_lear=[]
                self.dict_lear.append(user_answer)
                data =pandas.DataFrame( self.dict_lear)
                data.to_csv("learn.csv")

    def position_state(self,user_answer):
        self.post_state=self.data[self.data.state==user_answer]
        self.x_pos=int(self.post_state["x"])
        self.y_pos=int(self.post_state["y"])
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(x=self.x_pos,y=self.y_pos)
        turtle.write(arg=f"{user_answer}",font=("Arial",10,"normal"))




