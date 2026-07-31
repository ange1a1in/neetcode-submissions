class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if edges != node - 1
        if len(edges) != n - 1: # no cycle
            return False
        
        graphs = collections.defaultdict(list)
        # create graph
        for start, end in edges:
            graphs[start].append(end)
            graphs[end].append(start)
        
        queue = deque([])
        visited = {0}
        queue.append(0)
        while len(queue) > 0:
            curr = queue.popleft()
            neighbors = graphs.get(curr, [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return len(visited) == n # no isolated node
