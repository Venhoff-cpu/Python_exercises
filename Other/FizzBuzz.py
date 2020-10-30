for i in range(1, 101):
    fizz = 'Fizz' if i % 3 == 0 else ''
    buzz = 'Buzz' if i % 5 == 0 else ''
    print(f"{fizz}{buzz}" or i)


def fizz_buzz_generator(n):
    for _ in range(1, n+1):
        if _ % 3 == 0 and _ % 5 == 0:
            yield 'FizzBuzz'
        elif _ % 3 == 0:
            yield 'Fizz'
        elif _ % 5 == 0:
            yield 'Buzz'
        else:
            yield _


for fizbuzz in fizz_buzz_generator(100):
    print(fizbuzz)
