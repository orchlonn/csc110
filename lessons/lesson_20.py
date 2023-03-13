# str1 = "apple"
# str2 = "I love school"

# ListOfWord = str2.split()

# for word in ListOfWord:
#     print(word)
    

def count_words_in(sentence):
    sentence = sentence.lower()
    split_words = sentence.split()
    vowels = "aeiou"
    
    for word in split_words:
        if len(word ) > 3 and len(word) < 7:
           for i in vowels:
               if i in word:
                    #   add
                   last = word[-1]
                   if last == 'y':
                    return word

print(count_words_in("I lovey apple"))


testString = "stand firm in the faith"
lastChar = testString[-1]










def count_vowels(Word):
    vowels = "aeiou"
    Word = Word.lower()
    counter = 0
    for letter in Word:
        if letter in vowels:
            counter += 1

    return counter
        
def count_words_in(sentence):
    list_of_words = sentence.split()
    counter = 0
    
    for word in list_of_words:
        if 3 <= len(word) <= 7 and count_vowels(word)>=2:
            print(word,len(word))
            counter += 1
    return counter
