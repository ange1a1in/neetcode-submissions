# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        res = []
        res.append(str(root.val))
        queue = deque([root])

        while len(queue) > 0:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
                res.append(str(curr.left.val))
            else:
                res.append('#')
            if curr.right:
                queue.append(curr.right)
                res.append(str(curr.right.val))
            else:
                res.append('#')
        while res[-1] == "#": 
            # delete more'#'
            res.pop(-1)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        print(data)
        nums = data.split(',') # string to list
        root = TreeNode(nums[0])
        queue = deque([root])
        i = 1

        while i < len(nums) and len(queue) > 0:
            curr = queue.popleft()
            if i < len(nums) and nums[i] != '#':
                curr.left = TreeNode(nums[i])
                queue.append(curr.left)
            i += 1

            if i < len(nums) and nums[i] != '#':
                curr.right = TreeNode(nums[i])
                queue.append(curr.right)
            i += 1
        
        return root

