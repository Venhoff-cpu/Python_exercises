from collections import Iterable


def deep_flatten(seq):
    """
    Deep flattening the list. We check whether successive elements of the list are iterable and not a string
    or an entity (wo don't won't to yield single letters).
    If they are iterable we call the generator deep_flatten again.
    :param seq: Sequence for flattening
    :return: Every element of the sequence
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
