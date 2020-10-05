from collections.abc import Sequence, MutableSet, Set


class OrderedSet(Sequence, MutableSet):
    """Set-like object that maintains insertion order of items.
    Inheriting after Sequence to get accses to methods such as __reverse__, index, count.
    Implementation of __iter__ after __getitem__.
    """
    def __init__(self, iterable):
        self.items = set()
        self.order = []
        # relies on an in-place union (|=) to update the ordered set properly
        # (this delegates to our add method which maintains insertion order and uniqueness)
        self |= iterable

        # Not needed after implementing in-place union.
        # for item in iterable:
        #     if item not in self.items:
        #         self.items.add(item)
        #         self.order.append(item)

    def __getitem__(self, item):
        return self.order[item]

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def add(self, item):
        if item not in self.items:
            self.items.add(item)
            self.order.append(item)

    def discard(self, item):
        if item in self.items:
            self.items.discard(item)
            self.order.remove(item)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return (
                len(other) == len(self) and
                all(x == y for x, y in zip(self, other))
            )
        return super().__eq__(other)
