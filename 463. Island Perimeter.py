class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        perim = 0

        def dfs(r, c):
            nonlocal perim
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c]==0:
                return False
            if (r,c) in visited:
                return True

            visited.add((r,c))
            if not dfs(r+1, c):
                perim += 1

            if not dfs(r-1, c):
                perim += 1

            if not dfs(r, c+1):
                perim += 1

            if not dfs(r, c-1):
                perim += 1

            return True

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)

        return perim