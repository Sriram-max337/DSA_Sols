class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        x = 1
        n = len(word)

        def dfs(r, c):
            nonlocal x

            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited:
                return False

            if x == n:
                return True

            visited.add((r, c))

            if r + 1 < rows and board[r + 1][c] == word[x]:
                x += 1
                if dfs(r + 1, c):
                    return True
                x -= 1

            if r - 1 >= 0 and board[r - 1][c] == word[x]:
                x += 1
                if dfs(r - 1, c):
                    return True
                x -= 1

            if c + 1 < cols and board[r][c + 1] == word[x]:
                x += 1
                if dfs(r, c + 1):
                    return True
                x -= 1

            if c - 1 >= 0 and board[r][c - 1] == word[x]:
                x += 1
                if dfs(r, c - 1):
                    return True
                x -= 1

            visited.remove((r, c))
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j):
                        return True

        return False