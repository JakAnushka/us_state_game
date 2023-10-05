import turtle
from turtle import Screen
from state_access import state
screen=Screen()
turtle.title("U.S. States Games")
image="blank_states_img.gif"
states = state()
screen.bgpic(image)
# taking input from user in game.
game_is_on = True
while game_is_on:
    input_answer = screen.textinput(title=f"Guess the state {states.score}/50", prompt="What the another state name?")
    user_answer= input_answer.title()
    states.check_answer(user_answer)
    states.position_state(user_answer)
    if states.score==50:
        game_is_on=False




screen.exitonclick()
