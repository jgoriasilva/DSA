from typing import *
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        solved = {}
        queue = deque()
        directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0: 
                    solved[(i,j)] = 0
                    queue.extend([(i+dx, j+dy) for dx, dy in directions if 0 <= i+dx < rows and 0 <= j+dy < cols and mat[i+dx][j+dy] != 0])
                else:
                    mat[i][j] = rows*cols
        while len(queue):
            i, j = queue.popleft()
            if (i, j) in solved: continue
            res = rows*cols
            for dx, dy in directions:
                if (i+dx, j+dy) in solved:
                    res = min(res, mat[i+dx][j+dy])
                elif 0 <= i+dx < rows and 0 <= j+dy < cols:
                    queue.append((i+dx, j+dy))
            mat[i][j] = 1 + res
            solved[(i,j)] = mat[i][j]
        return mat

# mat = [[0],[0],[0],[0],[0]]
mat = [[0], [1]]
solution = Solution().updateMatrix(mat)
print(mat)