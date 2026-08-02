class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # use heap as value in graph
        heap = []
        res = []

        if not tickets:
            return res

        graph = defaultdict(list)
        for from_, to in tickets:
            heapq.heappush(graph[from_], to)
        
        def dfs(node):
            while graph[node]:
                next_ = heapq.heappop(graph[node])
                dfs(next_)
            res.append(node)
        
        dfs('JFK')

        return res[::-1]
        # reverse




