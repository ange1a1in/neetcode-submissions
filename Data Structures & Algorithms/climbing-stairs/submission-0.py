class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            # i == n：刚好到顶，找到 1 种有效走法，返回 True
            # i > n：走过头了，这条路无效，返回 False
            if i == n:
                return 1
            if i > n:
                return 0
    
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        return dfs(0)
