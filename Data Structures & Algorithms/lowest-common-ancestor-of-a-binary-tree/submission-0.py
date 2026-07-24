# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = self.dfs(root, p, q)
        return res[1]

    def dfs(self, root, p, q):
        # return type: (count, commonAncestor)
        if not root:
            return (0, None)
        
        leftCount, leftNode = self.dfs(root.left, p, q)
        rightCount, rightNode = self.dfs(root.right, p, q)

        # count = 2
    
        if leftCount == 2:
            return (2, leftNode)
        
        if rightCount == 2:
            return (2, rightNode)

        selfCount = 0
        if root == p or root == q:
            selfCount = 1

        count = selfCount + leftCount + rightCount

        if count == 2:
            return (2, root)

        return (count, None)


