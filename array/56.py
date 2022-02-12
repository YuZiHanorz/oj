class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res =[]; lt =intervals[0][0]; rt = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= rt:
                rt = max(rt, intervals[i][1])
            else:
                res.append([lt, rt])
                lt = intervals[i][0]; rt = intervals[i][1]
        res.append([lt, rt])
        return res
