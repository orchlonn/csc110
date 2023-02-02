
    


import turtle

def ONEsquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

def main():
    t = turtle.Turtle()

    size = 20
    for i in range(5):
        ONEsquare(t, size)
        t.penup()
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.pendown()
        size += 20


main()