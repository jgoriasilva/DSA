class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLength = 0

        hashmap = {}
        for i, c in enumerate(s):
            if c in hashmap:
                maxLength = max(maxLength, len(hashmap))
                pointer = hashmap.pop(c) + 1
            else:
                hashmap[c] = i

        maxLength = max(maxLength, len(hashmap))
        
        return maxLength


s = "dvdf"

print(Solution().lengthOfLongestSubstring(s))
