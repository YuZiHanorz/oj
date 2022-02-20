'''
class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = [0 for _ in range(len(height))]
        maxh = res = 0
        for i in range(len(height)):
            maxl[i] = maxh
            maxh = max(maxh, height[i])
        maxh = 0
        for i in range(len(height)-1, -1, -1):
            res += max(min(maxl[i], maxh)-height[i],0)
            maxh = max(height[i], maxh)
        return res
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = maxr = res = 0
        lt = 0; rt = len(height) - 1
        while lt < rt: # when lt = rt, all is concerned
            if height[lt] < height[rt]: # maxl also less than h_rt
                if height[lt] > maxl:
                    maxl = height[lt] # leak from left
                else:
                    res += maxl - height[lt]
                lt += 1
            else:
                if height[rt] > maxr:
                    maxr = height[rt] # leak from right
                else:
                    res += maxr - height[rt]
                rt -= 1
        return res
