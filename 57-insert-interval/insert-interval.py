class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        overlapped_list = []
        for i in newInterval:
            overlapped_list.append(i)
        fresh_list = []

        l2 = [i for i in range(newInterval[0],newInterval[-1] + 1)] 

        for interval in intervals:
            l1 = [i for i in range(interval[0],interval[-1] + 1)] 
            if not set(l1).isdisjoint(l2): # overlapps
                overlapped_list = overlapped_list + list(l1)
            else:
                fresh_list.append(interval)
        

        mi = min(overlapped_list)
        mx = max(overlapped_list)
        new_interval = [mi,mx]
        fresh_list.append(new_interval)
        fresh_list.sort()
        return fresh_list



        