class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lt = 0; rt = len(numbers) - 1
        while lt <= rt:
            cur = target - numbers[lt]
            while lt <= rt and cur < numbers[rt]:
                rt -= 1
            if numbers[rt] == cur:
                return [lt+1, rt+1]
            lt += 1
