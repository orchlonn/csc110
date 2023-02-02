# Problem 1
# 1)
# Quinton
# Erdenetuya
# orchlon 

# 2)
import math
import random
def find_z(x):
    z = math.pi **2 / math.sqrt(3 * x)
    return z

# 3)
real_number = random.uniform(1,3)
result = find_z(real_number)
print("Random numbers between 1 to 3 is", real_number, "and the result of the function is", result)

# Problem 2
# 1)
import turtle 

def ONEpentagon(t,a): 
    for i in range(5):
        t.forward(a)
        t.left(72)

# 2)
t = turtle.Turtle()
for i in range(5):
    random_number = random.randint(12, 100)
    ONEpentagon(t, random_number)
    t.penup()
    t.right(360 / 6)
    t.pendown()
