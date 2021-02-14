def with_previous(seq, *, fillvalue=None):
    """Provide each iterable item with item before it."""
    prev_item = fillvalue
    for item in seq:
        yield item, prev_item
        prev_item = item
