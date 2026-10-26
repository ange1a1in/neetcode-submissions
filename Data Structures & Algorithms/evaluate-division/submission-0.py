class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # a/b = value as a directed edge from a to b with weight value, and an edge from b to a with weight 1/value

        # build an adjacency list where each variable maps to a list of (neighbor, weight) pairs
        adj = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        
        def bfs(src, target):
            # if either variable is not in the graph, return -1
            if src not in adj or target not in adj:
                return -1
            # initialize a queue with (src, 1.0) and a visited set
            q, visit = deque([(src, 1)]), set()
            visit.add(src)

            while q:
                # dequeue a node and its accumulated weight
                node, w = q.popleft()
                if node == target:
                    return w
                for nei, weight in adj[node]:
                    if nei not in visit:
                        q.append((nei, w * weight))
                        visit.add(nei)
            return -1

        return [bfs(q[0], q[1]) for q in queries]
