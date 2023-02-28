def newtonSqrt(n, howmany):
    approx = 0.5 * n
    while True:
        betterApprox = 0.5 * (approx + n / approx)
        if approx == betterApprox:
            break
        approx = betterApprox
        
    return betterApprox


print(newtonSqrt(100, 10))