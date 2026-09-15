class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        no_of_islands = 0
        visited = set()
        i,j = 0,0

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j]=="0" or (i,j) in visited:
                return
            visited.add((i,j))
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1" and (x,y) not in visited:
                    no_of_islands += 1
                    dfs(x,y)

        return no_of_islands