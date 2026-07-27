class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        temp = []
        candidates.sort()
        self.dfs(candidates, target, result, temp, 0)
        return result

    def dfs(self, candidates, target, result, temp, startIndex):
        if sum(temp) == target:
            result.append(temp + [])
            return
        
        if sum(temp) > target:
            return
        
        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i-1]:
                continue
            num = candidates[i]
            temp.append(num)
            self.dfs(candidates, target, result, temp, i+1)
            temp.pop(-1)
        

    
