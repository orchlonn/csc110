# fullname=input('enter your full name')

# split_names = fullname.split()

# print(split_names)

import string 

def numChar(char):
    return string.ascii_lowercase.find(char) + 1

print(numChar('a'))
print(numChar('b'))
print(numChar('c'))