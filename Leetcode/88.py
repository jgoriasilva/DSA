from typing import *

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m > 0 and n > 0:
            nums1 = nums1[:m]
            nums1.extend(nums2)
            nums1.sort()
        elif m > 0:
            pass
        elif n > 0:
            nums1 = nums2
        else:
            pass

solution = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

solution.merge(nums1, m, nums2, n)