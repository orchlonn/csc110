list1 = []
list2 = []

for i in range(1,21):
    if i % 2 == 0 and i % 3 == 0:
        print(i, "divided both 2 and 3")
        list1.append(i)
    elif i % 2 == 0 or i % 3 == 0:
        print(i, "divided both 2 or 3")
        list2.append(i)
    else:
        print(i, "not divided neither 2 nor 3")

import random
user = input("Do you want to play? (y/n) ")

if user == "y":
    prompt_number = int(input("Enter integer between 1 - 10? "))
    rand_interger = random.randint(1, 10)
    if rand_interger == prompt_number:
        print("Have a nice day!")    
    else: 
        print("Goodbye")