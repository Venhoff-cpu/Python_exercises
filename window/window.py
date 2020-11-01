from collections import deque


def window(iterable, n, *, fillvalue=None):
    if n == 0:
        return
    iterator = iter(iterable)
    current = deque(maxlen=n)
    for _ in range(n):
        current.append(next(iterator, fillvalue))
    yield tuple(current)
    for item in iterator:
        current.append(item)
        yield tuple(current)
