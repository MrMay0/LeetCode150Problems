class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        profit = 0
        for price in prices[1:]:
            diff = price - min_price
            if diff > profit:
                profit = diff
            if price < min_price:
                min_price = price
        return profit