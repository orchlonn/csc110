import math

def distance(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    c = a ** 2 + b ** 2
    return math.sqrt(c)

hyptonesis = distance(2, 2, 6, 5)
print(round(hyptonesis, 2))


# find the triangle area
def trnglArea(x1, y1, x2, y2, x3, y3): 
    a = distance(x1,y1,x2, y2)
    b = distance(x2,y2,x3, y3)
    c = distance(x1, y1, x3, y3)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

area = trnglArea(2, 2, 6, 5, 6, 2)

print(round(area, 2))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

# animal list
animals = ['cat', 'dog', 'bird', 'lion', 'tiger']

# add 'guinea pig' to animal list
animals.append('guinea pig')

print(animals)