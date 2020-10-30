import unicodedata
from collections import UserString
from functools import total_ordering


def normalize_case_insensitive(text):
    return unicodedata.normalize("NFKD", text.casefold())


@total_ordering
class FuzzyOrderingMixin:

    def __lt__(self, other):
        return normalize_case_insensitive(self.data) < normalize_case_insensitive(other)

    def __eq__(self, other):
        return normalize_case_insensitive(self.data) == normalize_case_insensitive(other)


# We have to practice multiple inheritance using a "mixin" class to get total_ordering
# to work because the UserString class implements the other comparisons by default,
# so total_ordering will ignore them and won't actually do anything useful for us if we just
# decorated our FuzzyString class directly.
class FuzzyString(FuzzyOrderingMixin, UserString):
    """String which compares in a case-insensitive way."""

    # def __add__(self, other):
    #     result = [self.data, other]
    #     return FuzzyString("".join(result))

    def __contains__(self, item):
        return normalize_case_insensitive(item) in normalize_case_insensitive(self.data)


my_word = FuzzyString("Hello!")
print(list(my_word.__dict__.values()))