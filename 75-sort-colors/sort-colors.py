class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = nums.count(0)
        count_one = nums.count(1)
        count_two = nums.count(2)
        total = count_zero + count_one + count_two
        
        nums[:] =  [0]*count_zero + [1]*count_one + [2]*count_two

        