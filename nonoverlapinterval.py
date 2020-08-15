class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end, cnt = float('-inf'), 0
        for i in sorted(intervals, key=lambda x: x[1]):
            if i[0] >= end: 
                end = i[1]
            else: 
                cnt += 1
        return cnt
