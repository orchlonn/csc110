
#! Question 1
# Write a function called check_inventory(inventory, low) that has as arguments a dictionary inventory containing the inventory of a fruit store, and low, an integer. The function returns a list of items that are below an inventory level that is given by the low integer parameter.
# Example: If the inventory is {'mango:22','banana':3,'apple':10}, check_inventory(inventory, 5) will return the list ['banana']. For the same inventory, check_inventory(inventory, 15) will return the list ['apple','banana'].

def check_inventory(inventory, low):
    low_inventory_items = []
    for item, count in inventory.items():
        if count < low:
            low_inventory_items.append(item)
    return low_inventory_items

inventory = {'mango': 22, 'banana': 3, 'apple': 10}
low = 5

low_inventory_items = check_inventory(inventory, low)
# print(low_inventory_items) 

low = 15
low_inventory_items = check_inventory(inventory, low)
# print(low_inventory_items)

#! Question 2 
# Build a dictionary with these words from English to Italian:
# wolf => lupo
# the => il
# cat => gatto
# and => e
# Write a function that takes a sentence in English and returns its translation as a string. Call the function with the following sentence:
# the cat and the wolf
# If a word is not found, print a message about it.

english_to_italian = {
    "wolf": "lupo",
    "the": "il",
    "cat": "gatto",
    "and": "e"
}

def translate_sentence(sentence):
    words = sentence.split()
    translated_words = []
    for word in words:
        if word in english_to_italian:
            translated_words.append(english_to_italian[word])
        else:
            print(f"Word '{word}' not found in dictionary.")
    return " ".join(translated_words)

sentence = "thde cats anda thfe waolf"
translation = translate_sentence(sentence)
print(translation)

#! Quesiton 3 
# Create a dictionary where the keys are the type of pizza and the values are the corresponding cost.
# Margherita => 12.00$
# Prosciutto => 15.00$
# Mushroom => 13.50$
# Rucola => 13.00$
# Using keys and values (you should not use “Margherita” etc.. other than in defining the dictionary), tell the user the cost of a pizza and ask them to enter the quantity they want to buy.
# Tell the user the total cost.
# For example, the output may look like this:
# Define the dictionary of pizza types and their prices

pizza_dict = {'Margherita': 12.00, 'Prosciutto': 15.00, 'Mushroom': 13.50, 'Rucola': 13.00}

total_cost = 0.0

for pizza_type, cost in pizza_dict.items():
    print(f"Cost of {pizza_type.lower()} pizza is {cost:.2f}$")
    quantity = int(input("How many would you like? "))
    total_cost += quantity * cost

print(f"The total cost is {total_cost:.2f}$")