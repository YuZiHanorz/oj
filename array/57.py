class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            intervals.append(newInterval)
            return intervals
        st = newInterval[0]; ed = newInterval[1]
        for i in range(len(intervals)):
            if i == len(intervals) - 1 and st >= intervals[i][0]:
                if st > intervals[i][1]:
                    intervals.append([st, ed])
                else:
                    intervals[i][1] = max(intervals[i][1], ed)
                return intervals
            if st < intervals[i][0]:
                delpos = i
                if i > 0 and st <= intervals[i-1][1]:
                    delpos = i-1
                    st = intervals[i-1][0]
                print(st, intervals[i][0], i, delpos)
                for j in range(i, len(intervals)):
                    if j == len(intervals) - 1 and ed >= intervals[j][0]:
                        intervals[j][1] = max(ed, intervals[j][1])
                        del intervals[delpos:-1]
                        intervals[-1][0] = st
                        return intervals
                    if ed < intervals[j][0]:
                        if j == 0:
                            intervals.insert(i, [st, ed])
                            return intervals
                        else:
                            ed = max(ed, intervals[j-1][1])
                            del intervals[delpos:j]
                            intervals.insert(delpos, [st, ed])
                            return intervals
