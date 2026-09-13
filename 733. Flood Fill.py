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