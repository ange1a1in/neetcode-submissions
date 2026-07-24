class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        return[self.searchFirst(nums, target), self.searchLast(nums, target)]
    
    def searchFirst(self, nums:List[int], target: int):
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            if nums[mid] >= target:
                end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def searchLast(self, nums:List[int], target: int):
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid
            if nums[mid] > target:
                end = mid
        
        if nums[end] == target:
            return end

        if nums[start] == target:
            return start
        return -1

