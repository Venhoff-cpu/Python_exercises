SENTINEL = object()


def pluck(data, *paths, sep='.', default=SENTINEL):
    result = []
    for path in paths:
        value = data
        try:
            for key in path.split(sep):
                value = value[key]
        except KeyError:
            if default is SENTINEL:
                raise
            else:
                value = default
        result.append(value)

    return result[0] if len(result) == 1 else tuple(result)
