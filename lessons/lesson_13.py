def funciton1(n):
    if n % 11 == 0:
        return True
    else:
        return False

def isFactor(f, n):
    return n % f == 0 and 1 < f < n 

def factorsOf(n):
    for i in range(2, n):
        if isFactor(i, n):
            print(i)
            
list = []
def listOfFactors(n):
    for i in range(2, n):
        if isFactor(i, n):
            list.append(i)
    return list

list1 = []  
def func(f,l):
    for index in range(1, l):
        for i in range(2, f):
            if isFactor(i, f):
                list1.append(i)
        print(list1)
        list1 = []  

func(11,20)

def isPrimeNumber(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
               return True

            else:
              return True
    else:
      return  False
        
print(isPrimeNumber(11))