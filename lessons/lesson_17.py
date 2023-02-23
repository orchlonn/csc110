def match_digit(n, guess):
    guess_ten = guess // 10
    guess_one = guess % 10
    N_ten = n // 10
    N_one = n % 10
    
NComp = 37
cntr = 1
guess = int(input("Enter an integer 0-99:"))

while guess != NComp:
    digits = match_digit(NComp, guess)
    