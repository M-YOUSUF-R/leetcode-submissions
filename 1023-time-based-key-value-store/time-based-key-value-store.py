from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.ds = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ds:
            return ""
        
        pairs = self.ds[key]
        
        # Use binary search to find where this timestamp fits
        # bisect_right finds the first index where the stored timestamp > given timestamp
        idx = bisect.bisect_right(pairs, (timestamp, chr(127)))
        
        # If idx == 0, it means all stored timestamps are strictly greater than the given one
        if idx == 0:
            return ""
            
        # The correct value is at index idx - 1 (the largest timestamp <= given timestamp)
        return pairs[idx - 1][1]

        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)