from typing import *

"""
                                            _
                                        
                                        (       )      
                                    True,() False,[]
                                    ((      ()
                                False,[] True,() 
                                        ()(     ())
                                    False,[] False,[]

"""



class Solution:
    def recursive(self, seq: str, n: int, c_open: int, c_close: int, res: List[str]) -> List[str]:
        if c_open == c_close == n:
            res.append(seq)
            return res
        if c_open < n:
            res = self.recursive(seq+'(', n, c_open+1, c_close, res)
        if c_close < c_open:
            res = self.recursive(seq+')', n, c_open, c_close+1, res)

        return res

    def generateParenthesis(self, n: int) -> List[str]:
        res = self.recursive('', n, 0, 0, [])
        return res  

n = 3

res = Solution().generateParenthesis(n)

print(res)
