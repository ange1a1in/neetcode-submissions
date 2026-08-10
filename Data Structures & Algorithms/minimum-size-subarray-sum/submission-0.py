class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        sums = 0

        min_len = len(nums) + 1
        for j in range(len(nums)):
            sums += nums[j]
            while sums >= target:
                sums -= nums[i] # 把左边i移除
                min_len = min(j-i+1, min_len)
                i += 1

        # corner case: 全加起来也比target小
        if min_len == len(nums) + 1:
            return 0
        
        return min_len