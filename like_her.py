import turtle

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('red')
turtle.bgcolor('gray')

move_speed = 20
turn_speed = 15

def aage():
    turtle.forward(move_speed)

def peeche():
    turtle.backward(move_speed)

def daaye():
    turtle.right(turn_speed)

def baaye():
    turtle.left(turn_speed)


turtle.shape('turtle')
turtle.fillcolor('yellow')
turtle.goto(0,0)
turtle.speed(0)
#turtle.penup()

screen.onkey(aage, 'Up')
screen.onkey(peeche, 'Down')
screen.onkey(daaye, 'Right')
screen.onkey(baaye, 'Left')
screen.listen()
