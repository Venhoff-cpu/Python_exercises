import re


def parse_ranges(ranges):
    for string in ranges.split(','):
        m = re.search(r'\d*(->)\w+', string)

        if m is None:
            start, find, end = string.partition('-')
            if find:
                yield from range(int(start), int(end) + 1)

            else:
                yield int(string)
        else:
            start, find, _ = string.partition('->')
            yield int(start)

# Different approach with separated functions
# def partition(sep, group):
#     group = re.sub(r'->.*', r'', group)
#     a, _, b = group.partition(sep)
#     return ((a, b) if b else (a, a))
#
# Different approach using generator comprehensions
# def parse_ranges(ranges_string):
#
#     pairs = (
#         partition('-', group)
#         for group in ranges_string.split(',')
#     )
#     return (
#         num
#         for start, stop in pairs
#         for num in range(int(start), int(stop)+1)
#     )


# PAIRS_RE = re.compile(r'( \d+ ) - ( \d+ )', re.VERBOSE)
#
# def parse_ranges(ranges_string):
#     """Return iterable based on comma-separated numeric ranges."""
#     return [
#         num
#         for start, stop in PAIRS_RE.findall(ranges_string)
#         for num in range(int(start), int(stop)+1)
#     ]
