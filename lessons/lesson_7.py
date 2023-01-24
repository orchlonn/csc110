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

print(random.random())




