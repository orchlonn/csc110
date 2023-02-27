
#! Question 1
# Write a function, untilEqual() that rolls an 8-sided dice 2 times, and stops when both dice are equal. Computer rolls the dice using the random module and uses a WHILE loop. Score starts at 1000, every roll of the 2 dice that does not produce equal values, debits score by 5. Your function must return the final score.

# In a for loop, call the function 10 times and, for each time, print the score. Calculate the average score and print the result in a sentence.
# import random

# def untilEqual():
#     score = 1000
#     while True:
#         roll_input1 = random.randint(1, 8)
#         roll_input2 = random.randint(1, 8)
#         if roll_input1 == roll_input2:
#             break
#         score -= 5
#     return score

# final = 0
# for i in range(10):
#     score = untilEqual()
#     final += score
#     print(f"Score {i+1}: {score}")
# average_score = final / 10
# print(f"Average score: {average_score}")

#! Question 2
# # with a sentinel-controlled while loop, ask the user for numbers and print out the largest of the numbers given by the user without using the built-in function max.

# largest_num = 0

# while True:
#     num = float(input("Enter a number (or 0 to quit): "))
#     if num == 0:
#         break
#     if num > largest_num:
#         largest_num = num

# print("The largest number is:", largest_num)

#! Question 3

# Write a program for an ATM that will validate the user’s PIN. Here are some specifications:
# During the loop, ask the user to enter their PIN. If you enter your PIN incorrectly, increment the amount of attempts by 1.
# If you fail to enter the PIN 3 times, the program tells the user the account has been locked and exits.
# If you enter the correct PIN, the program tells the user access is granted and exits.
# Define the correct PIN

correct_pin = "0000"

# Initialize the number of attempts
attempts = 0

# Loop until the user enters the correct PIN or runs out of attempts
# while attempts < 3:
#     # Ask the user to enter their PIN
#     pin = input("Enter your PIN: ")
#     # Check if the PIN is correct
#     if pin == correct_pin:
#         print("Access granted.")
#         break
#     else:
#         attempts += 1
#         if attempts < 3:
#             print("Incorrect PIN. Please try again.")
#         else:
#             print("Account locked.")
            
            
#! Question 4 
# Optional (1 point extra credit):
# At the end of week 4, we wrote a function that returned the approximated Euler number e^x (see video and/or slides and/or code posted that week).
# Change that function (or write a new one) that uses a WHILE loop and RETURNs the number of terms needed to approximate the Euler’s number e to within 0.001.
# Use math.e from the math module to compare your approximation.
import math

def approx_e():
    approximation = 1
    term = 1
    n = 1
    while abs(math.e - approximation) > 0.001:
        term *= 1 / n
        approximation += term
        n += 1
    return n

print(approx_e())