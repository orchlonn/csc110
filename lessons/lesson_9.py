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
    a = x2- x1
    b = y2 - y1
    c = distance(x3, y3, x1, y1)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

area = trnglArea(2, 2, 6, 5, 3, 3)

print(round(area, 2))