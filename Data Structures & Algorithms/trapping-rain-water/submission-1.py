class Solution:
    def trap(self, height: List[int]) -> int:
        # see a bar that is taller than the bar on top of the stack
        # means we've found a right wall for a container
        # the bar we pop is the bottom, and the new top of the stack becomes the left wall

        if not height:
            return 0
        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(right, left) - mid
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res
