class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      #Boyer-Moore majority vote alg
        cnt = cand = 0
        for num in nums:
            if cnt == 0:
                cand = num
                cnt += 1
            elif cand == num:
                cnt += 1
            else:
                cnt -= 1
        return cand
