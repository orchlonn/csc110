
#! Question number 1
#The following steps calculate the balance after 3 years when $500 is deposited in a savings account. The balance is incremented every year according to the following:

#Create the variable “balance” and assign it the value 500.

#After the 1st year, the value of “balance” increases by 3%.

#After the 2nd year, the value of “balance” increases by 1%.

#After the 3rd year, the value of “balance” increases by 2%.

#Write a sentence displaying the final value of “balance”, rounded to two decimal places.

balance = 500
balance = balance +  (balance / 100 * 3)
balance = balance +  (balance / 100 * 1)
balance = balance + (balance / 100 * 2)

print(round(balance, 2))


#! Question number 2
#Convert the number below into a string and write, in a sentence, how many digits it contains, e.g. “The number 34592934 has 8 digits”.

#Note that your code should work for any number, that is, inside the print function, use the variable x instead of the actual number. The number 8 must be the result of your code and cannot be written manually.

x = 34592934
str_var = str(x)
length = len(str_var)
print("The number", str_var, "has", length, "digits")