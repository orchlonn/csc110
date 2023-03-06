# str1 = "apple"
# str2 = "I love school"

# ListOfWord = str2.split()

# for word in ListOfWord:
#     print(word)
    

def count_words_in(sentence):
    split_words = sentence.split()
    for word in split_words:
        if len(word ) > 3 and len(word) < 7:
            return word

print(count_words_in("I love apple"))
