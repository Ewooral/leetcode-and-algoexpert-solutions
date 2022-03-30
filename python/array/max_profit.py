"""
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""
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
