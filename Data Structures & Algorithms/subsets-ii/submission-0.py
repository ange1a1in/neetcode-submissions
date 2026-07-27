class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        nums.sort()
        self.dfs(nums, path, result, 0)
        return result
    
    def dfs(self, nums, path, result, startIndex):
        result.append(path + []) # deep copy

        for i in range(startIndex, len(nums)):
            if i > startIndex and nums[i] == nums[i-1]:
                # avoid duplicates
                continue 
            path.append(nums[i])
            self.dfs(nums, path, result, i+1)
            path.pop(-1)