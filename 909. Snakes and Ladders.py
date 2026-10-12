class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        reverse = False
        flat_board = []
        for i in range(len(board)-1,-1,-1):
            if reverse:
                flat_board.extend(board[i][::-1])
            else:
                flat_board.extend(board[i])
            reverse = not reverse

        min_moves = 0
        start = curr = 0
        destination = len(flat_board)-1

        def bfs(flat_board, start, destination, curr):
            nonlocal min_moves
            queue = deque([start])
            visited = {start}
            while queue:
                for i in range(len(queue)):
                    curr = queue.popleft()
                    if curr == destination:
                        return min_moves
                    for j in range(curr+1, min(curr+6, destination)+1):
                        if flat_board[j] != -1: 
                            next_pos = flat_board[j]
                            if next_pos-1 not in visited:
                                visited.add(next_pos-1)
                                queue.append(next_pos-1)
                        else:
                            if j not in visited:
                                visited.add(j)
                                queue.append(j)
                min_moves += 1
            return -1

        return bfs(flat_board, start, destination, curr)