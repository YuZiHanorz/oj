class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lt = [0 for _ in range(len(prices))]
        rt = [0 for _ in range(len(prices))]
        minp = prices[0]
        for i in range(1, len(prices)):
            minp = min(minp, prices[i])
            lt[i] = max(lt[i-1], prices[i] - minp)
        ma = prices[len(prices) - 1]
        for i in range(len(prices)-2, -1, -1):
            ma = max(ma, prices[i])
            rt[i] = max(rt[i+1], ma - prices[i])
        for i in range(len(prices)):
            lt[i] += rt[i]
        return max(lt)
