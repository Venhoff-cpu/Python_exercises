def give_change(to_give):
    coins = [1, 2, 5]
    n = 0
    result = 0
    while to_give > 0:
        for i in coins:
            if to_give >= coins[i] > n:
                n = coins[i]

        to_give -= n
        result += 1

    return result
