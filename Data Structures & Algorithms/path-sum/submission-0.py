# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = self.dfs(root, targetSum)
        return targetSum in res

    def dfs(self, root, targetSum):
        # return type: [path]

        if not root:
            return []
        
        if root.left is None and root.right is None:
            return [root.val]
    
        
        leftSumList = self.dfs(root.left, targetSum)
        rightSumList= self.dfs(root.right, targetSum)

        res = []
        
        for val in leftSumList:
            res.append(val + root.val)
        for val in rightSumList:
            res.append(val + root.val)

        return res

