
#! Question 1
# Give the logical opposites of these conditions. You are not allowed to use the not operator. For example print(“The logical opposite of a == b is a != b”).

# No need to assign values to the variables.

# 1. x < y
# 2. x >= y
# 3. x <= 18  and  day == 3
# 4. x >= 18  or  day != 3

print("The logical opposite of x < y is x >= y")

print("The logical opposite of x >= y is x < y")

print("The logical opposite of x <= 18 and day == 3 is x > 18 or day != 3")

print("The logical opposite of x >= 18 or day != 3 is x <= 18 and day == 3")


#! Question 2
# Make a truth table for “(x and y) or (not x)”. An example (see slides and video) is posted (see Week 5 - Wednesday).

# Note: your code should generate this truth table with for loops. Include a table header.

# x    y   (x and y)    (not x)    (x and y) or (not x)
# -----------------------------------------------------
print("x\ty\t(x and y)\t(not x)\t(x and y) or (not x)")
print("--------------------------------------------------")

for x in [True, False]:
    for y in [True, False]:
        result = (x and y) or (not x)
        print(f"{x}\t{y}\t{x and y}\t{not x}\t{result}")
        
#! Question 3
# A fruit company sells oranges for 32 cents a pound. They charge $7.50 for shipping on any order. But, if the order is above 50 pounds, they only charge $5 for shipping. Even better, if the order is over 100 pounds, the shipping charge is only $3.

# Write a function cost_order(pounds) that takes the number of pounds of oranges that is being purchased and returns the total cost of the order (including shipping costs).

# Example: a call of cost_order(60) (ordering 60 pounds of oranges) would return a cost of $24.20

# Note that this assignment has a built-in unit test so it gives you feedback as you run it.
def cost_order(pounds):
    cost_per_order = 0.32 * pounds
    if pounds <= 50:
        cost_per_order += 7.5
    elif pounds <= 100:
        cost_per_order += 5
    else:
        cost_per_order += 3
    return cost_per_order

print(cost_order(60))

#! Question 4
# 1. With the append method, create a list1 of all integers from 2 to 250 that are not divisible by 5 and are not divisible by 4.

# 2. Then, create a list2 with a similar program where the condition is modified using DeMorgan’s law (it should generate the same numbers).

# Print list 1 and list 2.

# Calculate the sum and the average of one of the lists. Do NOT use the sum accumulator this time. You do not need to write a function.

myList1 = []
myList2 = []

for i in range(2, 251):
    if i % 5 != 0 and i % 4 != 0:
        myList1.append(i)
    if i % 5 == 0 or i % 4 == 0:
        continue
    myList2.append(i)

print("List 1:", myList1)
print("List 2:", myList2)

sum_list1 = sum(myList1)
avg_list1 = sum_list1 / len(myList1)

print("Sum of List 1:", sum_list1)
print("Average of List 1:", avg_list1)