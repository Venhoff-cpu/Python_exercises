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


def dec_list():
    getcontext().prec = 2
    return [i for i in range_float()]


if __name__ == "__main__":
    # Lista będzie składac się z wartosci typu decimal z zadana dokładnością
    my_list = dec_list()
    print(my_list)
    print(f'Czy wszytkie elementy listy sa typu deciaml? {all(isinstance(item, Decimal) for item in my_list)}')

# Alternatywnie można skorzystać z biblioteki NumPy i funkcji arange
# import numpy as np
#
#
# def dec_list():
#     getcontext().prec = 2
#     return [Decimal(i) for i in np.arange(2, 6, 0.5)]
#
# if __name__ == "__main__":
#     # Lista będzie składac się z wartosci typu decimal.
#     my_list = dec_list()
#     print(my_list)
#     print(f'Czy wszytkie elementy listy sa typu deciaml? {all(isinstance(item, Decimal) for item in my_list)}')
