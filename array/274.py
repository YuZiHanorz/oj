class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        curcnt = 0
        bigger = 0
        for i in range(len(citations)-1, -1, -1):
            curcnt += 1
            if i == 0 or (i > 0 and citations[i-1] != citations[i]):
                if bigger <= citations[i] <= bigger + curcnt:
                    return citations[i]
                elif citations[i] < bigger:
                    return bigger
                bigger = curcnt + bigger
                curcnt = 0
        return len(citations)
