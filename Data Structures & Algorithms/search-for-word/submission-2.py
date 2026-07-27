class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        visited = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, board, 0, word, visited):
                    return True
        return False

    def dfs(self, i, j, board, index, word, visited):
        if index < len(word) and word[index] != board[i][j]:
            # 检查当下这个格子符不符合 word
            return False
        if index == len(word) - 1:
            # 一路匹配到了最后一个letter了，就终止
            return True

        visited.add((i,j))

        for (di, dj) in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            newi = i + di
            newj = j + dj
            if self.isValid(newi, newj, board, visited):
                if self.dfs(newi, newj, board, index+1, word, visited):
                    return True
        visited.remove((i,j))

    def isValid(self, i, j, board, visited):
        return 0<=i<len(board) and 0<=j<len(board[0]) and (i, j) not in visited

