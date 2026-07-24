# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = self.dfs(root)
        return res[0]


    def dfs(self, root):
        # return type: (maxLen, Desc, Incr)

        if not root:
            return (1, 0, 0)

        leftMaxLen, leftDesc, leftIncr = self.dfs(root.left)
        rightMaxLen, rightDesc, rightIncr = self.dfs(root.right)
        
        rootDesc, rootIncr = 0, 0

        if root.left:
            if root.left.val + 1 == root.val:
                rootDesc = max(rootDesc, leftDesc + 1)
            if root.left.val - 1 == root.val:
                rootIncr = max(rootIncr, leftIncr + 1)
        
        if root.right:
            if root.right.val + 1 == root.val:
                rootDesc = max(rootDesc, rightDesc + 1)
            if root.right.val - 1 == root.val:
                rootIncr = max(rootIncr, rightIncr + 1)
        
        rootMaxLen = max(rootIncr + rootDesc + 1, leftMaxLen, rightMaxLen) 

        return (rootMaxLen, rootDesc, rootIncr)