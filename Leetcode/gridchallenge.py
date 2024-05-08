def gridChallenge(grid):
    
    n, m = len(grid), len(grid[0])
    if n == 1:
        return 'YES'
    
    for i in range(n):  # O(n)
        grid[i] = ''.join(sorted(grid[i]))  # O(m*logm)
        
    for i in range(1, n):  # O(n)
        for j in range(m):  # O(m)
            if ord(grid[i][j]) < ord(grid[i-1][j]):
                return 'NO'
            
    return 'YES'

grid = ['eabcd',
'fghij',
'olkmn',
'trpqs',
'xywuv']

res = gridChallenge(grid)
print(res)