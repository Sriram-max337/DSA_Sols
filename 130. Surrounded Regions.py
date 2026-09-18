class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols or (i,j) in visited or board[i][j] == "X":
                return
            visited.add((i,j))
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        for x in range(rows):
            for y in range(cols):
                if (x == 0 or x == rows-1 or y == 0 or y == cols-1) and (x,y) not in visited and board[x][y] == "O":
                    dfs(x,y)

        for a in range(rows):
            for b in range(cols):
                if (a,b) not in visited and board[a][b] == "O":
                    board[a][b] = "X"