# # While loop
# isTrue = False
# inp = input('Enter your choice [1 - 4]')
# while inp not in ['1', '2', '3', '4']:
#     print('That is ont a valid choice')
#     inp = input('Enter your choice [1 - 4]')
    

# if inp == '4':
#     print("Have a great day.")     
# else:
#     print("Your order will be right up")
    
i = 0
avr = 0
while i < 4:
   num = int(input('Enter a number '))
   avr += num
   i += 1

print(avr / 4)