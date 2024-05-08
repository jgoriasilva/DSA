from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        biggest = nums[0]
        count_repetition = 0
        count = 0
        for i, n in enumerate(nums):
            if n == biggest and count_repetition >= 2:
                nums[i] = float('inf')
                count_repetition += 1
            elif count_repetition < 2:
                count_repetition += 1
                biggest = n
                count += 1
            elif n != biggest:
                count_repetition = 1
                biggest = n
                count += 1
        nums.sort()
        nums[:] = nums[:count]


solution = Solution()

nums = [0,0,1,1,1,1,2,3,3]

solution.removeDuplicates(nums)