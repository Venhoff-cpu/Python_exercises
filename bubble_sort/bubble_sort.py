def bubble_sort(A):
    """

    :param A: a list of numbers to sort
    :return: list A sorted in ascending order
    """
    n = len(A)
    while n > 0:

        for i in range(0, n-1):
            if A[i]>A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

        n -= 1

    return A


if __name__ == "__main__":
    sort_this = [10, 2, 3, 4, 6, 9, 22, 1, 0, 30, 21]
    print(bubble_sort(sort_this))