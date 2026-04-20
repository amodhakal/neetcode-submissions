import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = math.inf
        max_profits = 0

        for r in range(0, len(prices)):
            current = prices[r]
            if lowest_price > current:
                # found a lowest price
                lowest_price = current
                continue

            profit = current - lowest_price
            if profit < 0:
                # No profit
                continue

            if profit > max_profits:
                # Found a bigger profit
                max_profits = profit
        

        return max_profits