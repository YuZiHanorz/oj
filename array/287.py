class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0 # x_(i+1) = f(x_i) = nums[i]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        start = 0
        while True:
            start = nums[start]
            slow = nums[slow]
            if start == slow:
                return slow
# https://www.cnblogs.com/grandyang/p/4843654.html
