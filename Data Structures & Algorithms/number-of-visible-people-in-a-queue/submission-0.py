class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = []

        for i in range(n):
            maxi = cnt = 0
            for j in range(i + 1, n):
                if min(heights[i], heights[j]) > maxi:
                    cnt += 1
                maxi = max(maxi, heights[j])
            
            res.append(cnt)
        return res