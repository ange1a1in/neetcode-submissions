class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []
        # create nums list
        nums = [i for i in range(1, n+1)]
        self.dfs(nums, path, result, 0, k)
        return result
    
    def dfs(self, nums, path, result, startIndex, k):
        if len(path) == k:
            result.append(path + [])
            return


        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.dfs(nums, path, result, i + 1, k)
            path.pop(-1)