# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = self.dfs(root)
        return res[1]

    def dfs(self, root):
    # return type: (maxHeight, isBalanced)
        if not root:
            return (0, True)
        
        leftH, isLeftBal = self.dfs(root.left)
        rightH, isRightBal = self.dfs(root.right)

        currentBal = abs(leftH - rightH) < 2 and isLeftBal and isRightBal

        currentH = max(leftH, rightH) + 1
        return (currentH, currentBal)



