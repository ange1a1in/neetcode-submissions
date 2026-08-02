class UnionFind:
    def __init__(self, n):
        self.father = {}
        self.count = n
        for i in range(n):
            self.father[i] = i
    
    def find(self, x):
        if self.father[x] == x:
            return x
        currBoss = self.father[x]
        self.father[x] = self.find(currBoss)
        return self.father[x]

    def union(self, x, y):
        fatherX = self.find(x)
        fatherY = self.find(y)

        if fatherX != fatherY:
            self.father[fatherX] = fatherY
            self.count -= 1
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for edge in edges:
            uf.union(edge[0], edge[1])
        
        return uf.count


