class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # quick sort
        # pick pivot; partition; recursive both side
        # 递归的终止条件：如果这一段只剩 0 个或 1 个元素(start >= end),不用排,直接返回
        # partition：选一个 pivot,把这一段重新排布成"左边都 ≤ pivot,右边都 ≥ pivot"
        # 对左右两半递归：分别对左半段、右半段再调用一次快排。

        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, start, end):
        # base case
        if start >= end:
            return
        
        left, right = start, end
        pivot = nums[(left + right) // 2]

        while left <= right:
            # left 往右找"偏大的"(该去右边的)
            while left <= right and nums[left] < pivot:
                left += 1
            # right 往左找"偏小的"(该去左边的)
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # 第三步:对左右两半递归
        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)
            
        


