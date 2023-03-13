# import random 

# rand_number = random.randint(5, 10)
# total_roses = 35
# while(rand_number <= total_roses):
#     total_roses -= rand_number 
#     print("After selling {selled} roses, we have {left_roses}".format(selled = rand_number, left_roses = total_roses))
#     rand_number = random.randint(5, 10) 
# if total_roses > 0:
#     print("Roses left=", total_roses)



def word_detecter(words):
    words = words.split()
    
    for i in range(len(words)):
        word = words[i]
        if word[0] == 'o' or word[0] == 'O' or word[0] == 'W' or word[0] == 'w':
            print(word)
        
word_detecter("Oh pray my wings are gonna fit me well")