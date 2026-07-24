class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else: 
                return mid
        
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        elif nums[end] < target:
            return end + 1
        
        