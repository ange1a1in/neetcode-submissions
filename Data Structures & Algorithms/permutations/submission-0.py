class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp = []
        result = []
        visited = set() # different with combinations
        self.dfs(nums, temp, result, visited)
        return result

    def dfs(self, nums, temp, result, visited):
        if len(temp) == len(nums):
            result.append(temp + [])
            return
        
        for i in range(0, len(nums)):
            # do not use index, but use visited
            if i in visited:
                continue
            num = nums[i]
            visited.add(i)
            temp.append(num)
            
            self.dfs(nums, temp, result, visited)

            visited.remove(i)
            temp.pop(-1)