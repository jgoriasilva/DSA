class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= 0: return not x
        max_ten = 0
        while x // 10**max_ten > 0: max_ten += 1 
        max_ten -= 1
        l, r = max_ten, 0
        while r < l:
            if x // 10**l != x // 10**r: return False
            l -= 1
            r += 1
        return True

x = 121

print(Solution().isPalindrome(x))