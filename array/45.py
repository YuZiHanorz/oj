class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        hashmap = {}
        hashmap[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j not in hashmap:
                    hashmap[i+j] = 1 + hashmap[i]
                else:
                    hashmap[i+j] = min(hashmap[i+j], hashmap[i] + 1)
        return hashmap[len(nums) - 1]
        '''
        
        cursteps = 0
        rt = 0 ##the farthest within cursteps
        maxidx = 0 ##the farthest within curstep + 1
        if len(nums) <= 1:
            return 0
        for i in range(len(nums)):
            maxidx = max(maxidx, i + nums[i])
            if i == rt:
                cursteps += 1
                rt = maxidx
                if rt >= len(nums) - 1:
                    return cursteps
