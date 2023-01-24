import turtle

orchlon = turtle.Turtle()
orchlon.shape('turtle')
bg = turtle.Screen()
orchlon.penup()
orchlon.stamp()

bg.bgcolor('light green')
orchlon.color('blue')

orchlon.penup()
orchlon.forward(100)
orchlon.pendown()
orchlon.forward(10)
orchlon.penup()
orchlon.forward(15)


for i in range(12):
    orchlon.penup()
    orchlon.forward(100)
    orchlon.pendown()
    orchlon.forward(10)
    orchlon.penup()
    orchlon.forward(15)
    orchlon.penup()
    orchlon.stamp()
    #orchlon.backward(115)
    orchlon.goto(0, 0)
    orchlon.left(360 / 12)

a = 100
b = 50
c = 35
r1 = 30
r2 = 120
r3 = 90

orchlon.left(r1)
for i in range(6):
    orchlon.forward(a)
    orchlon.right(r2)
    orchlon.forward(b)
    orchlon.right(r3)
    orchlon.forward(c)
    orchlon.right(150)