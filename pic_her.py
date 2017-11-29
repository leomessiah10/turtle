import turtle

turns = 90
wn = turtle.Screen()
wn.setup(600,600)
wn.bgcolor('Black')

sqr = turtle.Turtle()
sqr.color('orange')
sqr.speed(0)

def square(length, turn):
    for i in range(4):

        sqr.forward(length)
        sqr.left(turn)
    
for times in range(50):
    square(150,turns)
    sqr.right(11)
