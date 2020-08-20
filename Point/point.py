class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __add__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1 + x2, y1 + y2, z1 + z2)

    def __sub__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1 - x2, y1 - y2, z1 - z2)

    def __mul__(self, other):
        x, y, z = self
        return Point(other * x, other * y, other * z)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return (x1, y1, z1) == (x2, y2, z2)

    def __repr__(self):
        return f"{type(self).__name__}(x={self.x}, y={self.y}, z={self.z})"
