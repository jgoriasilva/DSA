from typing import *

class Solution:

    def isAnagram(self, s:str, t:str):
        if len(s) != len(t):
            return False
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1
            if t[i] not in hashmap:
                hashmap[t[i]] = -1
            else:
                hashmap[t[i]] -= 1
        for c in s:
            if hashmap[c] != 0:
                return False
        return True

        # for s_letter in set(s):
        #     if s.count(s_letter) != t.count(s_letter):
        #         return False
        # return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = []
        while len(strs):
            word_i = strs[0]
            temp = [word_i]
            for word_j in strs[1:]:
                if self.isAnagram(word_i, word_j):
                    temp.append(word_j)
                    strs.remove(word_j)
            grouped.append(temp)
            strs.remove(word_i)

        return grouped


solution = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]

solution.groupAnagrams(strs)