
#! Question 1
# Using slicing and negative indices, print just “ght” from “Life Doesn’t Frighten Me”.
# Then, print “ght” with slicing and positive indices.
# With a for loop, traverse the string and print each letter, separately.
# With a for loop, traverse the string and print each word, separately.

text = "Life Doesn't Frighten Me"
print(text[-8:-5]) 
print(text[16:19]) 

for letter in text:
    print(letter)

for word in text.split():
    print(word)
    
    