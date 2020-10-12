def solution(S):
    string_len = len(S)
    groups = []
    num_of_splits = 3

    def gen_partitions(i):
        if i >= string_len:
            yield list(map(tuple, groups))
        else:
            if string_len - i > num_of_splits - len(groups):
                for group in groups:
                    group.append(S[i])
                    yield from gen_partitions(i + 1)
                    group.pop()

            if len(groups) < num_of_splits:
                groups.append([S[i]])
                yield from gen_partitions(i + 1)
                groups.pop()

    result = gen_partitions(0)

    result = [sorted(ps, key=lambda p: (len(p), p)) for ps in result]

    return result


print(solution('babaa'))
print(solution('ababa'))
