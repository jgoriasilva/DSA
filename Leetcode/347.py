"""

- Go once through array, count the occurence of each element and save it in a hashmap (dict).
- Sort the values of the hashmap keeping their respective keys in a descending order.
- Take the k first keys of the hashmap.

"""

from typing import

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        for num in nums:
            occurences[num] = occurences.get(num, 0) + 1
        
        sorted_occurences = sorted(occurences, key=occurences.get, reverse=True)

        return [*sorted_occurences][:k]


nums = [1,1,1,2,2,3]

Solution().topKFrequent(nums, 2)

              