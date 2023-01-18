c = 0  # initialize it

for i in ['a','z','q','2']:
    c += 1 # increases by one in every loop action no matter what is in the array

# print(c)

sum_acc = 0 # initialize it
list = [1, 3, 5, 7, 9]
for i in list:
    sum_acc += i # increases by the number in the array
    print('i =', i, 'sum_acc =', sum_acc)

average = sum_acc / len(list)
# print('Average =', average)


sum_acc2 = 0 # initialize it
counter = 0
for i in [1, 3, 5, 7, 2]:
    sum_acc2 += i # increases by the number in the array
    counter =+1
    # print('i =', i, 'sum_acc2 =', sum_acc2)
    
average = sum_acc2 / counter
print('Average =', average)


sum = 0
for i in range(1, 101):
    sum += i # increases by i

print('Total sum =', sum)
print(i * (i + 1) / 2 == 100 * 101 /2)
