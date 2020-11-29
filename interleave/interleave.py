from itertools import zip_longest


def interleave(*args):
    check_value = object()
    gen = (i
           for row in zip_longest(*args, fillvalue=check_value)
           for i in row
           if i is not check_value
           )

    return gen
