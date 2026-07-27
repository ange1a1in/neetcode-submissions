class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        temp = []
        candidates.sort()
        self.dfs(candidates, target, result, temp, 0, 0)
        return result

    def dfs(self, candidates, target, result, temp, startIndex, currSum):
        if currSum == target:
            result.append(temp + [])
            return
        
        if currSum > target:
            return
        
        for i in range(startIndex, len(candidates)):
            if i >= 1 and i > startIndex and candidates[i] == candidates[i-1]:
                continue
            num = candidates[i]
            temp.append(num)
            currSum += num
            self.dfs(candidates, target, result, temp, i+1, currSum)
            currSum -= num
            temp.pop(-1)
        

    
