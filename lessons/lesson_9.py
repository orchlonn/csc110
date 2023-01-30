import math

def distance(x1, y1, x2, y2):
    a = x2 - x1
    c = y2 - y1
    c = a ** 2 + c ** 2
    return math.sqrt(c)
    
hyptonesis = distance(2, 2, 6, 5)
print(round(hyptonesis, 2))
