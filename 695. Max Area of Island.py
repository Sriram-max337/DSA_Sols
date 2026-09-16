class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j]==0 or (i,j) in visited:
                return 0
            
            visited.add((i,j))
            a = dfs(i-1, j)
            b = dfs(i+1,j)
            c = dfs(i,j-1)
            d = dfs(i,j+1)
        
            return a + b + c + d + 1

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1 and (x,y) not in visited:
                    max_area = max(max_area, dfs(x,y))

        return max_area