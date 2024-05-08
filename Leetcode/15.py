from typing import *

class Solution:
    
    def _twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        left, right = 0, len(nums)-1
        triplets = []
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
                while left < len(nums)-1 and nums[left-1] == nums[left]:
                    left+=1
            elif nums[left] + nums[right] > target:
                right -= 1
                while right > 0 and nums[right+1] == nums[right]:
                    right-=1
            else:
                triplets.append([0-target, nums[left], nums[right]])
                left += 1
                while left < len(nums)-1 and nums[left-1] == nums[left]:
                    left+=1
            
        return triplets

    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # O(n logn)
        checked = set()
        triplets = []
        for i, num in enumerate(nums):
            if num in checked:
                continue
            triplets.extend(self._twoSum(nums[i+1:], 0-num))
            checked.add(num)
        
        return triplets
            

nums = [-1,0,1,0]

triplets = Solution().threeSum(nums)

print(triplets)
