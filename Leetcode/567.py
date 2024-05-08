class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = {}
        for c in s1: check[c] = 1 + check.get(c, 0)
        l, r = 0, 0
        for r in range(len(s2)):
            if check.get(s2[r], 0) == 0:
                if s2[l] in check and s2[l] != s2[r]: check[s2[l]] += 1
                l += 1
                # check = {k:v for k,v in original_check.items()}
            else:
                check[s2[r]] -= 1
                for v in check.values(): 
                    checked = True
                    if v != 0:
                        checked = False 
                        break
                if checked: return True
        return False

s1 = 'trinitrophenylmethylnitramine'
s2 = 'dinitrophenylhydrazinetrinitrophenylmethylnitramine'

print(Solution().checkInclusion(s1, s2))