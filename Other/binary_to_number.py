def bin_to_int(bin_num):
    return int(bin_num, 2)


def check_tuples(tup1, tup2):
    for a in tup1:
        if a not in tup2:
            return False

    return True


tup1 = (1, 4, 3)
tup2 = (1, 2, 3, 4)

print(check_tuples(tup1, tup2))


def f():
    x = 15
    print(x)


x = 12
f()


def alpha_to_ASCII(_string):
    result = ""
    for letter in _string:
        result += str(ord(letter))

    return int(result)


def remove_empty_lines(list_of_lines):
    return [line for line in list_of_lines if line]


def count_distinct_pairs(arr, k):
    count = 0
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] - arr[j] == k or arr[j] - arr[i] == k and (arr[i], arr[j]) not in pairs:
                count += 1
                pairs.append((arr[i], arr[j]))

    return count, pairs


def string_of_numbers(start, end):
    return "".join((str(i) for i in range(start, end+1)))


def list_with_unique_elements(arr):
    return list(set(arr))

print(remove_empty_lines(["Hi", "", "Hello", "", "5"]))
print(alpha_to_ASCII("abcd"))
print(count_distinct_pairs([1, 1, 3, 3, 5, 5, 6], 2))
print(string_of_numbers(0, 100))
print(list_with_unique_elements([1, 2, 3, 2, 4, 3]))