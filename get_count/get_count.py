import re


def count_words(sentence):
    regex = r"\w+\'\w+|\w+"
    words = re.findall(regex, sentence.lower())
    return {x: words.count(x) for x in words}


if __name__ == "__main__":
    print(count_words("oh what a day what a lovely day"))