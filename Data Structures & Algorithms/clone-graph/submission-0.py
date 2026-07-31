"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # edge case
        if node is None:
            return None

        # 把每一个原节点复制出一个新节点
        queue = collections.deque([node])
        maps = {}

        while len(queue) > 0:
            curr = queue.popleft()
            maps[curr] = Node(curr.val)
            for neighbor in curr.neighbors:
                if neighbor not in maps:
                    queue.append(neighbor)

        
        # 再遍历一边，把新节点之间的邻居关系补上
        for oldNode, newNode in maps.items():
            for old_nei in oldNode.neighbors:
                new_nei = maps[old_nei]
                newNode.neighbors.append(new_nei)
        return maps[node]

