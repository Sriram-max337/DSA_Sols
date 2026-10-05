class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init_pixel_color = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        r = sr
        c = sc
        if init_pixel_color == color:
            return image

        def dfs(image, rows, cols, r, c, color):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != init_pixel_color:
                return

            image[r][c] = color
            dfs(image, rows, cols, r-1,c, color)
            
            dfs(image, rows, cols, r+1, c, color)

            dfs(image, rows, cols, r, c-1, color)

            dfs(image, rows, cols, r, c+1, color)

            return image

        return dfs(image, rows, cols, r, c, color)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init_pixel_color = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        visited = set([(sr, sc)])
        queue = deque([(sr, sc)])

        r,c = sr,sc

        if init_pixel_color == color:
            return image
        image[sr][sc] = color

        def bfs(image, r, c):
            while queue:
                r,c = queue.popleft()
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and image[nr][nc]==init_pixel_color:
                        image[nr][nc] = color
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return image
        return bfs(image, r, c)