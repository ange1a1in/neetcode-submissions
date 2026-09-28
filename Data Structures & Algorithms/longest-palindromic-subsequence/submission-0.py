class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {} # create a memoization cache to store computed results

        def dfs(i, j):
            if i > j: # empty substring
                return 0
            if i == j: # single character length 1
                return 1
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == s[j]: # 两端字符相同 
                cache[(i, j)] = dfs(i + 1, j - 1) + 2
            else: # 两端字符不同
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j - 1))
            return cache[(i, j)]
        
        return dfs(0, len(s) - 1)