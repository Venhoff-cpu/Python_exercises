from collections import Iterable
from itertools import chain


def deep_flatten(seq):
    """
    Głębokie spłaszczanie listy. Sprawdzamy czy kolejne elemnty listy są ierowalne i nie są stringiem lub bytem.
    Jeśli są iterowalne, wywyołujemy ponownie generator deep_flatten.
    :param seq: sekwencja/lista do spłaszczenia
    :return: Spłaszczona wynikowa lista
    """
    for el in seq:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from deep_flatten(el)
        else:
            yield el

# Python 2.x
# def flatten(l):
#     for el in l:
#         if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
#             for sub in flatten(el):
#                 yield sub
#         else:
#             yield el