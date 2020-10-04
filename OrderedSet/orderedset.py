from collections.abc import MutableSet, Set


class OrderedSet(MutableSet):
    def __init__(self, itereable):
        self.items = set()
        self.order = []
        for item in itereable:
            if item not in self.items:
                self.items.add(item)
                self.order.append(item)

    def __iter__(self):
        return (item for item in self.order)

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
        if not isinstance(other, OrderedSet):
            return False
        else:
            return (
                len(other) == len(self) and
                all(x == y for x, y in zip(self, other))
            )
        return super().__eq__(other)
