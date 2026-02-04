import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's the state name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":

        to_be_guessed = []
        for state in all_states:
            if state not in guessed_states:
                to_be_guessed.append(state)
        df = pandas.DataFrame(to_be_guessed)
        print(df)
        df.to_csv("failed_to_guess.csv")

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)











