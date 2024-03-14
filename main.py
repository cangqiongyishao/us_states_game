import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. State Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)


data=pandas.read_csv('50_states.csv')
all_state=data.state.to_list()
guessed_states=[]
ct=0
while ct<50:
    answer_state=screen.textinput(title=f'{ct}/50 States Correct',prompt="What's another state's name?").title()

    if answer_state=='Exit':
        miss_states=[]
        for state in all_state:
            if state not in guessed_states:
                miss_states.append(state)
        new_data=pandas.DataFrame(miss_states)
        new_data.to_csv('state_to_learn.csv')
        break

    if answer_state in data['state'].values:
        state_data=data[data['state']==answer_state]
        guessed_states.append(answer_state)
        ct+=1
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto((int(state_data.x.iloc[0]),int(state_data.y.iloc[0])))
        t.write(answer_state)










# def get_mouse_click_coor(x, y):
#     print(x, y)
#

# turtle.onscreenclick(get_mouse_click_coor)
#
#
# turtle.mainloop()

# screen.exitonclick()
