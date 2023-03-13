# def num_words_in(Sentence):
#     Sentence = Sentence.split()
#     return len(Sentence)

# str = "A penny for your thoughts"
# result = num_words_in(str)

# print("There are", result, "words in,", str)


def longestWordIn(str):
    str = str.split()
    maxN = len(str[1])
    new_list = []
    for i in range(len(str)):
        if len(str[i]) >= maxN:
            maxN = len(str[i])

    for i in range(len(str)):
        if len(str[i]) == maxN:
            new_list.append(str[i])
    
    print(new_list)
    return maxN
    
    
    
    
print(longestWordIn("The darkest evening of the year"))