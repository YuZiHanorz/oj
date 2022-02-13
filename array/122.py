class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max1 = float('-inf'); max0 = 0
        for i in range(len(prices)):
            max1 = max(max1, max0-prices[i])
            max0 = max(max0, max1+prices[i])
        return max0
