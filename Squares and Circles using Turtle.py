import turtle

win = turtle.Screen()
win.bgcolor("black")

turt = turtle.Turtle()
turt.color("Red")
turt.speed(0)

def sqrcir(length,angle):
    for i in range(4):
        turt.backward(length)
        turt.left(angle)

# sqrcir(75,90)

for i in range(150):
    sqrcir(75,90)
    turt.left(11)
