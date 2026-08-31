class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        if len(intervals) == 1:
            return intervals
            
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        for interval in intervals[1:]:
            if  interval[0] <= prev[-1] : # overlapped
                prev[-1] = max(prev[-1],interval[-1])
            else:
                
                res.append(prev)
                prev = interval
        res.append(prev)
        return res


        