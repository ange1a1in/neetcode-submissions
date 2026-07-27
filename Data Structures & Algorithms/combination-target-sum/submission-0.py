class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        temp = []
        nums.sort()
        self.dfs(nums, temp, result, target, 0)
        return result

    def dfs(self, nums, temp, result, target, startIndex):
        if sum(temp) == target:
            result.append(temp + [])
            return
        
        if sum(temp) > target: 
            # early terminate 如果比target大了就不再重复加自己了
            return
        
        for i in range(startIndex, len(nums)):
            num = nums[i]
            temp.append(num)
            self.dfs(nums, temp, result, target, i) 
            # i instead of i+1 因为可以重复加自己
            temp.pop(-1)

