class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (index, temperature)
    
        for index, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                prev, j = stack.pop()
                res[j] = index - j
            stack.append((t, index))

        return res

    
