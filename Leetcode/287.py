from typing import *

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        # 5
        slow, fast = 0, 1
        # 2, 0
        while nums[slow] != nums[fast]:
            # 3, 4
            slow += 1
            fast += 2
            if slow == fast: continue
            if slow >= n:
                slow = 0
            if fast >= n:
                if n%2: 
                    fast -= n
                else:
                    fast = 1 if fast == n else 0
        
        return nums[slow]

nums = [4,3,1,4,2]

res = Solution().findDuplicate(nums)

print(res)