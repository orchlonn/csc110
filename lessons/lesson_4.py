# list & array is the fixed list. It means you can add element from the left, not the middle and first.
myList = [1,2,3,4,5]
list_length = len(myList)

#print(list_length)
counter = 0

for i in myList:
    counter += 1
    #print(counter)

#sqrt(x+6) - x / x^3 - 3x^2

q = 'Quinton'
k = 'kilian'
o = 'olivia'
orch = 'orchlon'
print('The students in our team are', q, 'and',k, 'and', o,'and', orch)

asked_cents = int(input())
quarter = asked_cents // 25

left_cents = asked_cents - (quarter * 25)

dime = left_cents // 10

left_cents = left_cents - (dime * 10)

nickel = left_cents // 5
left_cents = left_cents - (nickel * 5)


print(asked_cents, 'cents =>', quarter, 'Quarter(S)', dime, 'Dime(S)', nickel, 'Nickel(S)', left_cents, "Penny(S)")