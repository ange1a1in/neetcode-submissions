class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []
        visited = set()
        nums.sort()
        self.dfs(nums, temp, result, visited)
        return result
    
    def dfs(self, nums, temp, result, visited):
        if len(temp) == len(nums):
            result.append(temp+[])
            return
        
        for i in range(0, len(nums)):
            if i in visited:
                continue
            if i - 1 >= 0 and nums[i] == nums[i-1] and i-1 not in visited:
                continue
            num = nums[i]
            temp.append(num)
            visited.add(i)
            self.dfs(nums, temp, result, visited)
            visited.remove(i)
            temp.pop(-1)

