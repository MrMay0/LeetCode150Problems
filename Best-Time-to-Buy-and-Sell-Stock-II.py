class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2 : 
            return 0
        profit = 0
        prev_price = prices[0]
        for price in prices[1:]:
            diff = price - prev_price
            if diff > 0:
                profit += diff
            prev_price = price
        return profit