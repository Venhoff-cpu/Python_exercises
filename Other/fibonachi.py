def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter>n): return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(3)
for x in f:
    print(x)


def recur_fibonacci(n):
    if n<=0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return recur_fibonacci(n-1)+recur_fibonacci(n-2)
