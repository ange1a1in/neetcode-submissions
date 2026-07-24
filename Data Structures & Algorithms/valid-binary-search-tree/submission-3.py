# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = self.dfs(root)
        return res[2]

    def dfs(self, root):
        # return type: (minValue, maxValue, isValidBST)

        if not root:
            return (float("inf"), float("-inf"), True)
        
        leftMin, leftMax, leftIsBST = self.dfs(root.left)
        rightMin, rightMax, rightIsBST = self.dfs(root.right)

        minValue = min(leftMin, rightMin, root.val)
        maxValue = max(leftMax, rightMax, root.val)

        if rightIsBST and leftIsBST and leftMax < root.val < rightMin:
            isValidBST = True
        else: 
            isValidBST = False
        
        return (minValue, maxValue, isValidBST)

        


