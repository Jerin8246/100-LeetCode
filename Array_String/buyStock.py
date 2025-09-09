# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = prices[0]
#         max_profit = 0
#         for i in prices:
#             if i < min_price:
#                 min_price = i
#             if i - min_price > max_profit:
#                 max_profit = i - min_price
#         return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            if max_profit < prices[i] - min_price:
                max_profit =  prices[i] - min_price
        return max_profit