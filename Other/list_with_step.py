from decimal import Decimal, getcontext


# Domyślne wartości generatora zgodnie z poleceniem
def range_float():
    start = 2.0
    stop = 5.5
    step = 0.5

    count = 0
    # Pętla while - nie możemy użyć for, range nie akceptuje liczb zmienno przeciwnkowych (float)
    while True:
        value = Decimal(start + count*step)
        if value > stop:
            break
        count += 1
        yield value


if __name__ == "__main__":
    getcontext().prec = 2
    # Lista będzie składac się z wartosci typu decimal z zadana dokładnością
    my_list = [i for i in range_float()]
    print(my_list)
    print(f'Czy wszytkie elementy listy sa typu deciaml? {all(isinstance(item, Decimal) for item in my_list)}')

# Alternatywnie można skorzystać z biblioteki NumPy i funkcji arange
# import numpy as np
#
#
# if __name__ == "__main__":
#     getcontext().prec = 2
#     # Lista będzie składac się z wartosci typu decimal.
#     my_list = [Decimal(i) for i in np.arange(2, 6, 0.5)]
#     print(my_list)
#     print(f'Czy wszytkie elementy listy sa typu deciaml? {all(isinstance(item, Decimal) for item in my_list)}')
