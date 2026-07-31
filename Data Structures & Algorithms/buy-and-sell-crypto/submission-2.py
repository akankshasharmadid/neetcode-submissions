class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        profit = 0
        for i in prices:
            profit=max(0,profit,i-min_val)
            min_val = min(min_val,i)
        return profit