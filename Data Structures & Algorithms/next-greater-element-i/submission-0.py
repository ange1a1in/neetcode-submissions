class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # stack 后进先出
        stack = []
        maps = {} # (num and next-greater-num)

        for num in nums2:
            while stack and num > stack[-1]: # 拿当前数和"栈顶"比
                key = stack.pop() # 如果num比stack最后一个数大，就pop“栈顶”
                maps[key] = num
            stack.append(num)

        res = []

        for num in nums1:
            if num not in maps:
                res.append(-1)
            else:
                res.append(maps[num])
        return res

