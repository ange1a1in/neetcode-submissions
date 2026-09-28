class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # mark every reachable '0' as temporary 'T'
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs():
            q = deque()
            for row in range(rows):
                for col in range(cols):
                    if (row == 0 or row == rows - 1 or
                        col == 0 or col == cols - 1) and board[row][col] == 'O':
                        board[row][col] = 'T'
                        q.append((row, col))
                    
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'O'):
                        board[nx][ny] = 'T' 
                        q.append((nx, ny))

        bfs()
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'
        
