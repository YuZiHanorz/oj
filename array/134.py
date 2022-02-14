class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx = 0; mi = float('inf'); last = 0
        for i in range(len(gas)):
            val = gas[i] - cost[i]
            last = last + val
            if last < mi:
                mi = last
                idx = i + 1
        if last < 0:
            return -1
        if idx == len(gas):
            return 0
        return idx
