

"""class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums[:] = set(nums) # O(n)
        nums[:] = sorted(nums) # O(n logn)
        longest = float('-inf')
        previous = nums[0]
        count = 1
        for num in nums[1:]: # O(n)
            if num == previous + 1:
                count += 1
                longest = max(count, longest)
            previous = num
        
        return longest # O (n)"""

from collections import defaultdict
from typing import *

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums[:] = set(nums)

        left_side = {n:1 for n in nums}
        right_side = {n:1 for n in nums}
        
        longest = 1    
        for left in list(left_side):
            right = left-1
            if right in list(right_side):
                count = left_side.pop(left) + right_side.pop(right)
                left_side[right] = count
                right_side[left] = count
                longest = max(count, longest)


        for right in list(right_side):
            left = right+1
            if left in list(left_side):
                count = left_side.pop(left) + right_side.pop(right)
                left_side[right] = count
                right_side[left] = count
                longest = max(count, longest)

        return longest

nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]

Solution().longestConsecutive(nums)
