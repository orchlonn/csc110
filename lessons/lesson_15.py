
# deposit calculator
deposit = 10000
counter = 0
while deposit < 1000000:
    deposit += deposit * .04
    counter += 1

print(counter)

def func(x):
    return x**2 + 1

i = 1
while i < 5:
    print(func(i))
    # increased by 1
    i += 0.5

x = 1
for i in range(9):
    print(x, func(x))
    x += 0.5 

def helper(x):
    return x % 7 == 0 and x % 5 != 0 
inc = 1
for inc in range(100):
    ans = helper(inc)
    if (ans == True):
        print(inc)
        
