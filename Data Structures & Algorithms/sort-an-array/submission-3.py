class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums
    # 终止条件：如果这一段只剩 1 个元素(或 0 个),它本身就是有序的,直接返回,不用再切
    # 对半切,分别递归：找中点,把左半段和右半段各自先排好序(递归)。
    # merge：把两个已经排好序的半段,合并成一个排好序的整段。


    def mergeSort(self, nums, left, right):  
        # merge sort
        if left >= right:
            return
        
        mid = (left + right) // 2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid+1, right)
        self.merge(nums, left, mid, right)

    # 方法: 两个半段各放一个指针,都指向自己的开头。
    # 比较两个指针指的元素,谁小就把谁拿出来放进结果里,然后那个指针往后移一格。 
    # 一直比,直到某一边被拿空。最后把另一边剩下的直接接到结果后面(因为它本来就是有序的)。
    def merge(self, nums, start, middle, end):
        temp = [0] * (end - start + 1)
        left_index = start
        right_index = middle + 1
        index = 0
        
        # # 两边都还有元素时,比较,拿小的
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

        # 把排好的 temp 写回原数组对应区间
        nums[start:start + len(temp)] = temp 

        

