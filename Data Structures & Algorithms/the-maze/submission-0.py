class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = deque([start])
        visited = set()
        visited.add((start[0], start[1]))

        return self.bfs(maze, queue, visited, destination)

    def bfs(self, maze, queue, visited, des):
        while len(queue) > 0:
            x, y = queue.popleft()
            if x == des[0] and y == des[1]:
                return True

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newx, newy = x, y 
                # newx newy change back to x, y (need 4 direction up down left right)
                while self.couldPassBy(maze, newx+dx, newy+dy):
                    newx = newx + dx
                    newy = newy + dy
                if (newx, newy) not in visited:
                    visited.add((newx, newy))
                    queue.append((newx, newy))

        return False
                
    
    def couldPassBy(self, maze, x, y):
        return 0<=x<len(maze) and 0<=y<len(maze[0]) and maze[x][y] == 0


