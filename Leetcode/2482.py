class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        rows = [sum(row) for row in grid]
        columns = [sum(column) for column in zip(*grid)]
        diff = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j] = 2*(rows[i]+columns[j]) - len(grid) - len(grid[0])
        return diff

grid = [[0,1,1],[1,0,1],[0,0,1]]

print(Solution().onesMinusZeros(grid))