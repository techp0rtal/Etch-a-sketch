from turtle import Turtle, Screen, clearscreen, reset

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def reset_screen():
    clearscreen()
    reset()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="c", fun=reset_screen)
screen.exitonclick()