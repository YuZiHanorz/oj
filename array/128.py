class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for v in nums:
            s.add(v)
        maxcnt = 0
        while s:
            v = s.pop()
            cnt = 1
            lt = v - 1; rt = v + 1
            while lt in s:
                s.remove(lt)
                cnt += 1
                lt -= 1
            while rt in s:
                s.remove(rt)
                cnt += 1
                rt += 1
            maxcnt = max(cnt, maxcnt)
        return maxcnt
