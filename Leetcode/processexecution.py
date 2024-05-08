from ast import Continue
from typing import *


def getMaximumPower(nums: List[int]) -> int:
    maxPoints = float('-inf')

    for i in range(len(nums)):
        hashset = set()
        totalPoints = nums[i]
        hashset.add(nums[i]-1)
        hashset.add(nums[i]+1)
        for j, point in enumerate(nums):
            if i==j or point in hashset:
                continue
            else:
                totalPoints += point
                hashset.add(point-1)
                hashset.add(point+1)
        maxPoints = max(maxPoints, totalPoints)

    return maxPoints

nums = [3,7,10,5,2,4,8,9,9,4,9,2,6,4,6,5,4,7,6,10]

print(getMaximumPower(nums))