class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mai = 0 #profit of selling at day i
        mii = prices[0] #least price of stocks before day i
        for i in range(1, len(prices)):
            mai = max(mai, prices[i] - mii)
            mii = min(mii, prices[i])
        return mai
    
        
