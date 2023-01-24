# math library doing some math functions
import math 
# random library for generating random numbers
import random 

# ex-1: toss a coin
print(random.randrange(1, 7))

# ex:2  toss a coin 10 times
for i in range(10):
    print(random.randrange(0, 2))

# ex:3  Throw a 6-sided dice :
    print(random.randrange(1, 7))
    
# ex:4  Throw a 6-sided dice three times
for i in range(3):
    print(random.randrange(1, 7))


for i in range(5):
    print(random.random() * 100)

#def means that define the function 
def cube(N):
    y = N ** 3
    return y

x = 2
y = 5

print(cube(5), cube(2))
    
def converterFtoC(tempF):
     tempC = 5 / 9 * (tempF - 32)
     return tempC

fahr = 76
celcius = converterFtoC(fahr)

print(fahr, 'F =', celcius, 'C')


# find perimeter of a rectangle
def computePerimeter(sideA, sideB):
    return (sideA + sideB) * 2

sideA = 3 
sideB = 4
perimeter = computePerimeter(sideA, sideB)

print(sideA, sideB, 'perimeter =', perimeter)