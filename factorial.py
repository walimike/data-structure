def extra_long_factorial(n):
    x = 1
    mult = n
    while x < (n):
        mult *= (n-x)
        x += 1
    print(mult)

extra_long_factorial(25)
