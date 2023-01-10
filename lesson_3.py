# for loop is making events that can repeat many times as you want.

# In the example below it prints only integers.
for i in [1, 2, 3, 4, 5]:
    print(i)

# For this example, it prints everything in the list.
for i in ['d', 2, 3.5, 4/2, '5']:
    print(i)


# For loop examples below.
for i in [1, 2, 3, 4, 5]:
    print(i * 2)

for i in ["Jen", "Eli", "Sam"]:
    print(i +",how are you?")
    

# We can use range method instead of list of elements method. It begins with the 0.
#! FYI: Range method should include integer.
for i in range(2):
    print(i) # Result --> (0,1)


# It starts from first element in range method and only looping in range elements.
for i in range(1, 4):
    print(i) # Result --> (1,2,3)

# It starts from first element in range method and only looping in range elements and increases by the third element of range method.
for i in range(2, 10, 2): 
    print(i) # Result --> (2,4,6,8)

for i in range(2, -2, -1): 
    print(i) # Result --> (2,1,0,-1,-2)
    
for i in range(2, 6): 
    print(i, "squared =", i**2) # Result --> (4,9,16,25)

# show result in list
print(list(range(1, 10))) # Result --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10, 2))) # Result --> [1, 3, 5, 7, 9]
print(list(range(1, -3, -1))) # Result --> [1, 0, -1, -2]


