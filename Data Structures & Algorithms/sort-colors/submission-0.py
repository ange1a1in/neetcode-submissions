class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # fixed pointer 1 已经找到的0元素的下一位（表示这个元素之前的都是0）
        # fixed pointer 2 已经找到的2元素的上一位（表示这个元素之后的都是2）
        # 从左边swap到右边的，不用check，直接 +1，
        # 因为 float pointer 已经检查过了
        # 从右边swap到左边的，需要check，因为还没被检查到

        left, i = 0, 0 # left: fixed pointer; i: float pointer
        right = len(nums) - 1 # right: another fixed pointer

        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        while i <= right:
            if nums[i] == 0:
                swap(nums, i, left)
                i += 1 # left 比 right 多一个 i+=1
                left += 1
            elif nums[i] == 2:
                swap(nums, i, right)
                right -= 1
            elif nums[i] == 1:
                i += 1




