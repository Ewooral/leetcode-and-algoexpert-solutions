'''We want a function which accepts a very large list of prices(pricesLst) and returns the
largest possible loss a client could have made with only a buy transaction followed by a sell
transaction. The largest loss is calculated as pricesLst[index2] - pricesLst[index1] where
index1 < index2.
Please then write tests for this function to ensure it works as expected guarding against all
edge cases you can think of.'''


from more_itertools import grouper


def largest_possible_loss(prices_list):

    largest_loss = 0

    for purchase, sell in grouper(prices_list, 2):
        loss = abs(purchase) - abs(sell)
        if loss > largest_loss:
           largest_loss = loss

    return largest_loss


how_big_is_the_loss = largest_possible_loss([234, 32, 3, 44, 64, 1])
print(how_big_is_the_loss)



def max_loss(Prices):
    buy, sell = 0, 1     # index of the array
    maxLoss = 0
    while buy < len(Prices):
        if Prices[buy] > Prices[sell]:
            loss = Prices[buy] - Prices[sell]
            maxLoss = max(maxLoss, loss)
        else:
            sell = buy
        buy += 1
    return maxLoss


if __name__ == "__main__":
    print(max_loss([7, 1, 5, 3, 6, 4]))
    print(max_loss([234, 32, 3, 44, 64, 1]))


# O(N) T complexity
# O(1) S complexity
