def validate(*args):
    count = 0
    for arg in args:
        if count:
            if count != len(arg):
                raise ValueError("Given matrices are not the same size.")
        count = len(arg)
    return True


def add(*args):
    result = []
    validate(*args)

    for zip_list in zip(*args):
        validate(*zip_list)

        temp_list = [
            sum(ele)
            for ele in zip(*zip_list)
        ]
        result.append(temp_list)

    return result
