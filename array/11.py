class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''ma = 0
        for i in range(1, len(height)):
            for j in range(0, i):
                ma = max(ma, min(height[i], height[j]) * (i - j))
        return ma
        #brute force
        '''
        left = 0; right = len(height) - 1
        res = 0
        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]: 
                left += 1
            else:
                right -= 1
        return res
    '''if height[left] < height[right], then move right pointer leftwards will not contribute to the maximum since it must be smaller'''
