import re
import sys


def semantic_wrap(paragraph):
    result = re.sub(r'([.?!]"?)([ ]+)', r"\1\n", paragraph)
    return result


if __name__ == "__main__":
    with open(sys.argv[1]) as text_file:
        output = semantic_wrap(text_file.read())
    sys.stdout.write(output)