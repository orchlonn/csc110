# Write a program that simulates rolling a 16-sided die. Use a for loop to generate 10 random numbers from the 16-sided die (10 should be defined as a variable).

# Print those 10 numbers.

# Your program should calculate the sum and the average of those numbers using a sum accumulator.

# In a sentence, display the sum and average.

# Your code should work even if you change the number of random numbers generated.

import random
dice_side = 16
frequence = 10
sum = 0
for i in range(frequence):
    sum = sum + random.randrange(1,dice_side)
    
average = sum / frequence

print('Sum of the random 10 numbers is', sum, "and average is", average)



# Write a function areaOfCircle(r) which returns the area of a circle of radius r where r is a floating point datatype.

# Make sure you use the math module in your solution.

# Outside the function, generate a random real number between -3.0 and 3.0 (use random.random()). Invoke the function using the number randomly generated and print the result in a sentence like:

# Radius = [xx], Circle Area = [xx]
import math
import random
def areaOfCircle(r):
    area = math.pi * r * r
    return area

radius = random.uniform(-3.0, 3.0)
area = areaOfCircle(radius)
print('Radius = ', radius, ', Circle Area = ', area)