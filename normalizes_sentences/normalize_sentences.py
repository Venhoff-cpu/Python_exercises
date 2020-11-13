import re


# def normalize_sentences(text):
#     return (
#         text.replace('  ', '<d_space>')
#             .replace('. ', '.  ')
#             .replace('! ', '!  ')
#             .replace('? ', '?  ')
#             .replace('<d_space>', '  ')
#     )


def normalize_sentences(string):
    result = re.sub(r'(?<!\.\w)(?<![A-Z]\w)([.!?]) +', r'\1  ', string)
    # Make sure there's not a period two letters before us
    # Make sure there's not a honorific before punctuation
    # Sentence ending punctuation
    # One or more spaces
    return result
