# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.bfs(root, res)
        return res

        
    def bfs(self, root, res):
        queue = deque()
        queue.append(root)
        
        currLevel = 1
        while len(queue) > 0:
            size = len(queue)
            temp = []

            for _ in range(size):
                curr = queue.popleft()
                if curr:
                    if currLevel % 2 == 0:
                        temp.insert(0, curr.val)
                    else:
                        temp.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            currLevel += 1
            if temp:
                res.append(temp)
    


