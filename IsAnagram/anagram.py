from collections import Counter, defaultdict
from unicodedata import normalize
import re


regex_template = r'[^a-zA-Z]+'


def is_anagram(string1, string2):
    """Return True if the given words are anagrams."""
    string1 = re.sub(regex_template, '', normalize('NFKD', string1.lower()))
    string2 = re.sub(regex_template, '', normalize('NFKD', string2.lower()))

    return Counter(string1.lower()) == Counter(string2.lower())


# def letter_dict(word):
#     """Return dictionary of letters used in string. Custom implementation of Counter"""
#     letters = defaultdict(int)
#     for letter in word:
#         letters[letter] += 1
#
#     return letters
#
#
# def is_anagram(string1, string2):
#     """Return True if the given words are anagrams."""
#     string1 = re.sub(regex_template, '', normalize('NFKD', string1.lower()))
#     string2 = re.sub(regex_template, '', normalize('NFKD', string2.lower()))
#
#     return letter_dict(string1) == letter_dict(string2)


# def remove_accents(string):
#     """Return decomposed form of the given string."""
#     return unicodedata.normalize('NFKD', string)
#
# def letters_in(string):
#     """Return sorted list of letters in given string."""
#     string = remove_accents(string.lower())
#     return sorted(
#         char
#         for char in string
#         if char.isalpha()
#     )
#
# def is_anagram(word1, word2):
#     """Return True if the given words are anagrams."""
#     return letters_in(word1) == letters_in(word2)