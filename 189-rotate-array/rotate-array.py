import copy
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = copy.copy(nums)
        n = len(nums)
        for i in range(n):
            nums[(k+i)%n] = temp[i]
        
        
        