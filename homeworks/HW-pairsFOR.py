# This problem is not about ‘while loop. It’s about use a for loop with paired data (see example in Week 7 - Fri video/slides).

# There are various way to solve this problem. In this case, use paired data (i.e. 2 loop variables in the for loop).

# Use a for loop that prints the following output and count how many people like chocolate ice cream.

# Output:
# Sal likes vanilla ice cream
# Joy likes chocolate ice cream
# Eric likes mango ice cream
# Adam likes chocolate ice cream

# 2 people like chocolate ice cream

counter = 0
paired_data = [('Sal', 'vanilla'), ('Joy', 'chocolate'), ('Eric', 'mango'), ('Adam', 'chocolate')]

for i, type in paired_data:
    print(f"{i} likes {type} ice cream")
    if type == 'chocolate':
        counter += 1

print(f"\n{counter} people like chocolate ice cream")