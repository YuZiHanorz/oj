class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        localP = [0 for _ in range(k+1)]
        globalP = [0 for _ in range(k+1)]
        for i in range(1, n):
            diff = prices[i] - prices[i-1]
            for j in range(k, 0, -1):
                localP[j] = max(localP[j] + diff, globalP[j-1] + max(diff, 0))
                globalP[j] = max(globalP[j], localP[j])
        return globalP[k]
