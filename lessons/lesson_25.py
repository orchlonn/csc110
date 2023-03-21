import random
my_dict = {}

for i in range(1, 101):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    sumDice = roll1 + roll2
    my_dict[sumDice] += 1
    
for key in my_dict:
    print('Dice sum of', key, 'occurs', my_dict[key], 'times')
