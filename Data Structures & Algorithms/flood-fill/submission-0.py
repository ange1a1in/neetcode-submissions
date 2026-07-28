class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        self.bfs(image, sr, sc, color, image[sr][sc], visited)
        return image


    def bfs(self, image, i, j, newColor, oldColor, visited):
        if oldColor == newColor:
            return image
        
        queue = deque([(i, j)])
        image[i][j] = newColor
        while len(queue) > 0:
            i, j = queue.popleft()
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newi = i + di
                newj = j + dj
                if 0<=newi<len(image) and 0<=newj<len(image[0]) and image[newi][newj] == oldColor:
                    image[newi][newj] = newColor
                    queue.append((newi, newj))
        return image
            
        
    
