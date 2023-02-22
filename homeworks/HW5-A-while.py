
#! Question 1
# Write a function print_triangular_FOR(n) that prints out the first n triangular numbers with the for loop. Then write a similar function what uses the while loop print_triangular_WHILE(n). A call to either function would produce the following output:

def print_triangular_FOR(n):
    j = 1
    for i in range(1,n + 1):
        print(i, j)
        j += i + 1
        

def print_triangular_WHILE(n):
    i = 1
    j = 1
    while(i < n + 1):
        print(i, j)
        j += i + 1
        i += 1

# print_triangular_WHILE(5)
# print_triangular_FOR(5)

#! Qustion 2
# Create a function called howManyUntil(stopNum) where stopNum is an integer from 0 and 99

# The function will randomly generate a number from 0 and 99 and keep generating random numbers until the number stopNum is generated. The function will return the number of random numbers that were generated in order to get the stopNum. Use the while loop.

# Example: If stopNum = 50 and the random numbers generated were 0, 4, 19, 50, then the function would return 4.

import random
def howManyUntil(stopNum):
    input = random.randint(0,99)
    i = 0
    while(stopNum != input):
        i += 1
        input = random.randint(0,99)
        print(input)
    return i

# print(howManyUntil(50), 'ggggggg')

#! Question #3 
# Write a function drugPotency(loss, expire) that determines how many months a drug can remain in storage given a potency loss percentage (loss) and an expiration target (expire). For example, if a certain drug looses 4% of its effectiveness every month it is in storage, when its effectiveness is below 50% it is considered expired and must be discarded. The output from drugPotency(4.0, 50.0) would be:

def drugPotency(loss, expire):
    month = 0
    percentage = 100
    
    while expire < percentage:
        rounded_percentage = round(percentage, 10)
        print(f"Month:\t{month}\teffectiveness:\t{rounded_percentage}")
        percentage = percentage - percentage / 100 * loss
        month += 1
        
    if(expire > percentage):
        rounded_percentage = round(percentage, 10)
        print(f"Month:\t{month}\teffectiveness:\t{rounded_percentage}", "DISCARDED")
drugPotency(4, 50)