class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a = reduce(lambda x, y: x^y, nums) # x xor y with x != y
        res = [0, 0]
        a &= -a # find the minimum bit i where x[i] != y[i]
        for x in nums:
            if x & a: res[0] ^= x
            else: res[1] ^= x
        return res
