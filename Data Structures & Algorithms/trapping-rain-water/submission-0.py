class Solution:
    def trap(self, height: List[int]) -> int:
        
        water = 0
        stack = [] # (index)
        # right wall: 下一个大于或等于left wall高度的
        # 单调递减stack
        # 要有宽度差，才能存水

        for i, h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                stack_index = stack.pop()
            
                if stack:
                    width = i - stack[-1] - 1

                    # min(left, right) - bottom
                    newH = min(height[i], height[stack[-1]]) - height[stack_index]
                    water += newH * width
            stack.append(i)
            
        return water


