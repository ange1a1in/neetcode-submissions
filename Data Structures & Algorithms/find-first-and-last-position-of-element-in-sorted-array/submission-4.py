class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 找lower bound: 不直接找某个 target，而是找第一个 >= target 的位置
        # 如果 nums[m] >= target，m 可能就是答案，所以保留它：r = m。
        # 如果 nums[m] < target，m 和它左边都不可能是答案，所以：l = m + 1。
        # 最后 l == r，这个位置就是第一个 >= target 的索引。
        # 如果所有数都小于 target，就返回 len(nums)。

        n = len(nums)

        def binarySearch(target):
            left, right = 0, n
            while left < right:
                middle = (left + right) // 2
                if nums[middle] >= target:
                    right = middle
                else:
                    left = middle + 1
            return left
        
        start = binarySearch(target)
        if start == n or nums[start] != target:
            return [-1, -1]

        return [start, binarySearch(target + 1) - 1]


    
    
