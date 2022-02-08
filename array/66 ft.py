class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 0
        for i in range(len(digits)):
            if digits[i] != 9:
                flag = 1
                break
        if not flag:
            digits[0] = 1
            for i in range(1, len(digits)):
                digits[i] = 0 
            digits.append(0)
            return digits
        for i in range(len(digits)-1, -1, -1):
            if flag:
                if digits[i] < 9:
                    digits[i] += 1
                    flag = 0
                else:
                    digits[i] = 0
                    flag = 1
        return digits