# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = self.dfs(root)
        return res[2]
    
    def dfs(self, root):
        # return type: (sums, nums, maxAvg)
        if not root:
            return (0, 0, 0)

        leftsums, leftnums, leftMax = self.dfs(root.left)
        rightsums, rightnums, rightMax = self.dfs(root.right)

        nums = leftnums + rightnums + 1
        sums = leftsums + rightsums + root.val

        maxAvg = max(leftMax, rightMax, float(sums) / nums)

        return (sums, nums, maxAvg)
