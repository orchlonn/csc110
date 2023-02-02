
#! Question 1

# Write a function areaTrapezoid(base1,base2,height) that returns the area of a trapezoid with the parameters base1, base2 and height.

# Outside the function generate three random numbers between 10 and 150 for the dimensions of the trapezoid. Call the function to calculate the area and print the result in a sentence:

# The area of a trapezoid of base1 xxx, base2 xxx and height xxx is xxx.
import random
def areaTrapezoid(base1, base2, height):
    area = (base1 + base2) * height / 2
    print("The area of a trapezoid of base1 {}, base2 {} and height {} is {}".format(base1,base2,height,area))


random_inp_1 = random.randint(10,150)
random_inp_2 = random.randint(10,150)
random_inp_3 = random.randint(10,150)
areaTrapezoid(random_inp_1, random_inp_2, random_inp_3)

#! Question 2
# Write the function sumBetween(n,m) that returns the sum of all integer numbers starting at n and up to and including m. Invoke that function and print a the result in a sentence:

# The sum between xx and xxx is xxxx.

#! approach 1
def sumBetween(n, m):
    sum = 0
    for i in range(n, m + 1):
        sum += i
   
    return sum
n = 10
m = 15
result = sumBetween(n,m)
print("The sum between {} and {} is {}".format(n,m,result))

#! approach 2
def sumBetween(n, m):
    return sum(range(n, m + 1))

result = sumBetween(10, 15)
print("The sum of all integers between {10} and {15} is {result}.")


#! Question 3
# 1) Write a function regularPolygon(t,d,N) that uses a turtle t to draw a regular polygon with N sides of length d.

# Recall that the exterior angle of any polygon = 360/N (see following picture from the slides).

# https://1drv.ms/u/s!Aj8-mu701LOAgvgzARt9jZTl9Q5XUA?e=3wKCQE

# Make sure your function draws what you expect before moving to the next step.

# 2) Outside the function, in the main program, with a for loop, generate 4 random numbers between 3 and 10. For each number generated, call your function to draw a polygon with a number of sides equal to the random number generated.

# For example, if 4,10,5,3 are generated, then, a square, a decagon, a pentagon, a triangle are generated.

# The length of the side of the polygons is 40. After each polygon, move the turtle by some distance so there is some space between them.

# Here possible outputs:

# https://1drv.ms/u/s!Aj8-mu701LOAgvg0Aueov8amhIXx4A?e=eOjTTn

import turtle
import random

def regularPolygon(t, d, N):
    for i in range(N):
        t.forward(d)
        t.left(360/N)

t = turtle.Turtle()
for i in range(4):
    sides = random.randint(3, 10)
    regularPolygon(t, 40, sides)
    t.penup()
    t.forward(100)
    t.pendown()
    
    
#! Question 4
# 1) Write a function, Sphere_Vol(R), which returns the volume of a sphere with radius R.

# 2) Write a function, Sphere_Area(R), which returns the surface area of a sphere with radius R.

# 3) Use the above functions to make a table of the radius and the surface area divided by the volume of a sphere as shown in the link below (make a header, too, as shown). Round off the results to 2 decimal places.

# https://1drv.ms/u/s!Aj8-mu701LOAguUq0ZEh3UrrTgxADg?e=jIEnMR

import math
def Sphere_Vol(R):
    volume = 4 / 3 * math.pi * R**3
    return volume 

def Sphere_Area(R):
    area = 4 * math.pi * R**2
    return area 


def main():
    print("Radius  SA/Vol")
    print("-----   ------")
    for i in range(1, 10):
        R = i
        SA = Sphere_Area(R)
        Vol = Sphere_Vol(R)
        result = round(SA / Vol, 2)
        print(f"{R:<7} {result:<7}")
        
main()

#! Question 5
# Write a function ONEsquare(t, sz) where the turtle named t draws one square of size sz.

# Then call the function in a for loop to draw the concentric squares.

# Note that the function ONEsquare(t, sz) should draw only ONE square. The pattern should be made outside that function.

# Assume the innermost square is 20 units per side, and each successive square is 20 units bigger, per side, than the one inside it.

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