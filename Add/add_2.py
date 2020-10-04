def get_shape(matrix):
    return [len(r) for r in matrix]


def add(*args):
    shape_of_matrix = get_shape(args[0])
    if any(get_shape(m) != shape_of_matrix for m in args):
        raise ValueError("Given matrices are not of the same size.")
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*args)
    ]
