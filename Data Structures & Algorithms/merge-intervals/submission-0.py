class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # currStart(curr) and previousEnd(pre)

        intervals.sort()
        res = []

        for i, curr in enumerate(intervals):
            if i == 0:
                pre = curr
                continue

            # 比较currStart 和 previousEnd，看有没有 overlap
            if curr[0] > pre[1]: 
                # currStart 比 previousEnd 还大，那说明没有 overlap
                res.append(pre)
                pre = curr

            # 如果有 overlap
            else:
                # interval 的 end 等于 max(previousEnd, currEnd)
                pre[1] = max(pre[1], curr[1])
            
        res.append(pre)
        return res
