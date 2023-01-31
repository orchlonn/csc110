def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
    
def e_to_x_series(x, n):
    sum_acc = 0
    for i in range(n):
        sum_acc += x** i / factorial(i)
        # print(factorial(i))
    return sum_acc        

ans = e_to_x_series(1, 6)
print('X to e =',ans)

