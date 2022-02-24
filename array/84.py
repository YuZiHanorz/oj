class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ms = []
        maxa = 0
        for i in range(len(heights)):
            while ms and heights[ms[-1]] > heights[i]:
                idx = ms.pop(-1)
                h = heights[idx]
                w = i - ms[-1] - 1 if ms else i
                maxa = max(maxa, h * w)
            ms.append(i)
        while ms:
            idx = ms.pop(-1)
            h = heights[idx]
            w = len(heights) - ms[-1] - 1 if ms else len(heights)
            maxa = max(maxa, h * w)
        return maxa
