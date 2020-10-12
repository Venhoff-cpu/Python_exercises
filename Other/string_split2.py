from itertools import combinations


def solution(S):
    string_range = range(1, len(S))

    result = sum(
        1
        for start, end
        in combinations(string_range, 2)
        if 'a' in S[:start] and 'a' in S[start:end] and 'a' in S[end:]
    )

    return result


print(solution('babaa'))
print(solution('ababa'))
