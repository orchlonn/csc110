# find factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
input = int(input())
print('----------------')
for i in range(input):
    print(i + 1,'         ', factorial(i + 1))
