import math
import random

def functA(n1,n2):
    return True if n1 % n2 == 0 else False

def functB(n1,n2):
    return math.sqrt(n1**2 + n2**2)


for i in range(0,99):
    n1 = random.randint(40, 80)
    n2 = random.randint(10, 40)
    resultA = functA(n1,n2)
    resultB = functB(n1,n2)
    if resultA and resultB > 23:
        print(n1,n2)

i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i += 1

print(sum)

