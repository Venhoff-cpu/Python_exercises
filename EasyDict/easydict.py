from collections import UserDict


class EasyDict(UserDict):
    def __init__(self, my_dict={}, normalize=False, **items):
        self._normalized = normalize
        self.update(my_dict)
        self.update(items)

    @property
    def data(self):
        return self.__dict__

    def normalized(self, key):
        if self._normalized:
            return key.replace(" ", "_")
        else:
            return key

    def __getitem__(self, key):
        return self.__dict__[self.normalized(key)]

    def __setitem__(self, key, value):
        self.__dict__[self.normalized(key)] = value

    # When inheriting from UserDict there is no need for declaring __eg__ and get, as both methods are
    # already implemented in UserDict
    # def __eq__(self, other):
    #     if isinstance(other, self.__class__):
    #         return self.__dict__ == other.__dict__
    #     else:
    #         return False
    #
    # def get(self, key, default=None):
    #     try:
    #         return self.__dict__[self.normalized(key)]
    #     except KeyError:
    #         return default
