import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = dict.fromkeys(nums, 0)
        for num in nums:
            dic[num] += 1
        
        return max(dic,key=dic.get)