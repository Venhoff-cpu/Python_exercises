from collections import deque


def tail(seq, n=0):
    """Return the last n items of given sequence/iterable"""
    return list(deque(seq, maxlen=n)) if n > 0 else []
