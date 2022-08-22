import turtle
import pandas
import pandas as pd

from state_names import States_score
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
states_csv = "50_states.csv"
screen.addshape(image)
turtle.shape(image)
is_game_on = True
states_score = States_score()

#Import CSV for answers
state_data = pandas.read_csv(states_csv, index_col=False)
# print(state_data)
states_list = state_data["state"].to_list()
# print(states_list)

# game logic
answer_state = screen.textinput(title="Guess the state", prompt="Whats another state's name?").title()

while is_game_on:


    if answer_state in states_list:
        states_score.correct_answer(answer=answer_state)
        state = state_data[state_data.state == answer_state]
        # print(state)
        x_cor = state.x.item()
        # print(x_cor)
        y_cor = state.y.item()
        # print(y_cor)
        states_score.write_state(answer=answer_state, x= x_cor, y= y_cor)

    correct = states_score.amount_correct()
    amount_states = len(states_list)
    answer_state = screen.textinput(title=f"{correct}/{amount_states} States Correct", prompt="Whats another state's name?").title()

    if len(states_score.correct_guessed_states) > 50 or answer_state == "Exit" or "exit":
        is_game_on = False


#missed states to learn.csv
missing_states = []
for state in states_list:
    if state in states_score.correct_guessed_states:
        pass
    else:
        missing_states.append(state)

missing = {'Missing States': missing_states}

missing_df = pd.DataFrame(missing)

missing_df.to_csv('states_to_learn.csv')

turtle.mainloop()