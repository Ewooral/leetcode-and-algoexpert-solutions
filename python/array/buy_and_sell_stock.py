def buy_and_sell_stock(Prices):
    buy, sell = 0, 1     # index of the array
    maxProfit = 0 
    while sell < len(Prices):
        if Prices[buy] < Prices[sell]:
            profit = Prices[sell] - Prices[buy]
            maxProfit = max(maxProfit, profit)
        else:
            buy = sell
        sell += 1 
    return maxProfit


if __name__ == "__main__":
    print(buy_and_sell_stock([7, 1, 5, 3, 6, 4]))


# O(N) T complexity
# O(1) S complexity