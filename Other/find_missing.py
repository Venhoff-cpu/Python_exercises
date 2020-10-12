def find_missing(li, n):
    if not isinstance(n, int):
        return 'Wartośc n musi być liczbą całkowitą dlodatnią'

    if n <= 1:
        return 'Wartośc n musi być liczbą całkowitą dlodatnią większą od 1.'

    if not isinstance(li, list) and isinstance(li, str):
        return 'Do przeszukania należy podać listę'

    if not all(isinstance(item, int) for item in li):
        return 'Lista musi składać się z liczb całkowitych dodatnich.'

    if max(li) > n or min(li) < 1:
        return 'Lista poza przedziałem 1 - n'

    n_range = [i for i in range(1, n+1)]

    return [missing
            for missing in n_range
            if missing not in li]


if __name__ == '__main__':
    n = 10
    for_finding_missing = [1, 3, 4, 6]
    print(find_missing(for_finding_missing, n))
