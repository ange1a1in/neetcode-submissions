class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, left, right):  
        # merge sort
        if left == right:
            return
        
        mid = (left + right) // 2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid+1, right)
        self.merge(nums, left, mid, right)

    
    def merge(self, nums, start, middle, end):
        temp = [0] * (end - start + 1)
        left_index = start
        right_index = middle + 1
        index = 0

        while left_index <= middle and right_index <= end:
            if nums[left_index] < nums[right_index]:
                temp[index] = nums[left_index]
                index += 1
                left_index += 1
            else:
                temp[index] = nums[right_index]
                index += 1
                right_index += 1

        # 把剩余的元素，放进temp
        while left_index <= middle:
            temp[index] = nums[left_index]
            index += 1
            left_index += 1
        
        while right_index <= end:
            temp[index] = nums[right_index]
            index += 1
            right_index += 1

        nums[start:start + len(temp)] = temp 

        

