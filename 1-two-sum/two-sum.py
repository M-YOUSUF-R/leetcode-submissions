class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for key,val in enumerate(nums):
            complement = target - val
            if complement in seen:
                return [key,seen[complement]]
            seen[val] = key
