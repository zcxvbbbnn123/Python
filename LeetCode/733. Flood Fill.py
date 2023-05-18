class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        m, n = len(image), len(image[0])
        originalColor = image[sr][sc]
        if originalColor == color: return image
        
        #bfs using queue
        q = [[sr,sc]]
        while q:
            curr = q.pop(0)
            image[curr[0]][curr[1]] = color
            for direction in directions:
                nextPixel = [curr[0] + direction[0], curr[1] + direction[1]]
                if 0 <= nextPixel[0] < m and 0 <= nextPixel[1] < n:
                    if image[nextPixel[0]][nextPixel[1]] == originalColor:
                        q.append(nextPixel)
        return image

A = Solution()
print((A.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)))