class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        for i in range(len(numbers) - 1, 0,-1):
            gap = target - numbers[i]
            if gap in numbers:
                return sorted([i + 1 , numbers.index(gap) + 1])
        return []
