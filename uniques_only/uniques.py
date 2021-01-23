def uniques_only(seq):
    seen = set()
    seen_add = seen.add
    seen_unhashable = []
    for item in seq:
        try:
            if item not in seen:
                yield item
                seen_add(item)
        except TypeError:
            if item not in seen_unhashable:
                yield item
                seen_unhashable.append(item)

    # Method for Python 3.6+ for creating list with unique values.
    # return list(dict.fromkeys(seq))
