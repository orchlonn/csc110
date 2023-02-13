
#! Question 1
# Re-write the function below in a more compact way, i.e. the body of the function should only be ONE line of code.

def funct5(n):
       return True if n % 5 != 0 else False

print(funct5(32))

#! Question 2
# Write the Boolean function is_odd(n) that returns True when n is odd and False otherwise.

# Outside the function, generate 15 random integers with possible values from 1 to 30. Invoke the function and, for each number, print if the number is odd or not. For example:
# 7 is odd.
# 18 is not odd.
# etc..

import random 

def is_odd(n):
    return True if n % 2 == 0 else False
    

for i in range (0, 15):
    rand_inp = random.randint(1, 30)
    result = is_odd(rand_inp)
    if result:
        print(rand_inp, "is not odd")
    else: print(rand_inp, "is odd")
    
#! Question 3
# Modify the turtle bar chart program from the chapter 6.11 so that the bar
# for any value of 300 or more is filled with blue,
# values between [150 and 300) are filled yellow,
# and bars representing values less than 150 are filled magenta.
# Use it on the following data: xs = [150, 17, 80, 340, 160, 260, 220]

import turtle

def draw_bar(t, height):
    """Get turtle t to draw one bar, of height."""
    turtle.begin_fill()
    if height >= 300:
        turtle.fillcolor("blue")
    elif height >= 150:
        turtle.fillcolor("yellow")
    else:
        turtle.fillcolor("magenta")
    turtle.left(90)
    turtle.forward(height)
    turtle.write(" "+ str(height))
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

xs = [150, 17, 80, 340, 160, 260, 220]

orchlon = turtle.Turtle()          
orchlon.color("black")
orchlon.pensize(3)

for a in xs:
    draw_bar(orchlon, a)

turtle.done()
