class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quickSelect(nums, 0, len(nums) - 1, k)
        return nums[k-1]
    
    # quick select
    # pivot

    def quickSelect(self, nums, start, end, target):
        pivot = nums[(start + end) // 2]
        
        if start >= end:
            return
        
        left, right = start, end
        # sort 成降序，大的在前面
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if target <= left: # 看 left 的右边
            self.quickSelect(nums, start, right, target)
        if target >= right: 
            self.quickSelect(nums, left, end, target)

