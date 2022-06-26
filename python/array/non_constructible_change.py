def non_constructible_change(coins):
    coins.sort()
    # current_change_created = ccc
    ccc = 0
    for coin in coins:
        if coin > ccc + 1:
            return ccc + 1
        ccc += coin
    return ccc + 1


print(non_constructible_change([5, 7, 1, 1, 2, 3, 22]))