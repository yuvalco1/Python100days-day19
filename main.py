import random
from turtle import Turtle, Screen




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #tim = Turtle(shape="turtle")
    screen = Screen()
    #  commenting out early day project
    # def move_forwards():
    #     tim.forward(10)
    #
    # def move_backwards():
    #     tim.backward(10)
    #
    # def move_clockwise():
    #     tim.right(5)
    #
    # def move_c_clockwise():
    #     tim.left(5)
    #
    #
    # def clear_screen():
    #     tim.penup()
    #     tim.clear()
    #     tim.home()
    #     tim.pendown()
    #
    # screen.listen()
    # screen.onkey(key="w", fun=move_forwards)
    # screen.onkey(key="s", fun=move_backwards)
    # screen.onkey(key="a", fun=move_c_clockwise)
    # screen.onkey(key="d", fun=move_clockwise)
    # screen.onkey(key="c", fun=clear_screen)
    screen.setup(width=500, height=400)
    screen.title("Welcome to the turtle race!")
    user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ")
    #tim.penup()
    #tim.goto(x=-230, y=0)
    t_array = []
    colors = ("red", "green", "blue", "black", "yellow", "violet")
    for i in range(6):
        t_array.append(Turtle(shape="turtle"))
        t_array[i].color(colors[i])
        t_array[i].penup()
        t_array[i].goto(x=-230,y = (-150+i*60))
    if user_bet:
        is_race_on = True
    while is_race_on:
        for turtle in t_array:
            rand_distance = random.randint(0,10)
            turtle.forward(rand_distance)
            if turtle.position()[0] >= 235:
                winner = turtle.pencolor()
                print(winner)
                is_race_on = False
                break
    if winner == user_bet:
        print("You Won - the winner turtle is the "+winner+ " turtle !!")
    else:
        print("You Lost :-( - the winner turtle is the "+winner+ " turtle !!")
    screen.exitonclick()