c = 20



def fib(n):
    "try"
    a,b = 0,1
    while b < c:
        print b,
        a,b = b, a+b
    return b



print fib(1000)
