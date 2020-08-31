import argparse
import string


def count_upper_case(file):
    """
    Function for counting upper case letters in the text file.
    """
    with open("text") as text:
        count = sum(char.isupper() for char in text.read())
    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, action="store")
    options = parser.parse_args()
    print(count_upper_case(options.filename))


# class BigLetterCounter:
#     def __init__(self, filename):
#         self.filename = filename
#         self.counter = 0
#
#     def process_file(self):
#         with open(self.filename, "r") as input:
#             while True:
#                 char = input.read(1)
#
#                 if not char:
#                     break
#
#                 if char in string.ascii_upercase:
#                     self.counter += 1
