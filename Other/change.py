def give_change(to_give):
    coins = [1, 2, 5]
    n = 0
    result = 0
    given_coins = []
    while to_give > 0:

        for i in coins:
            if to_give >= i > n:
                n = i

        to_give -= n
        given_coins.append(n)
        result += 1
        n = 0

    return result, given_coins


if __name__ == '__main__':
    print(give_change(11))
