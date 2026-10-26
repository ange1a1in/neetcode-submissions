class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    def add_word(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
    
    def is_word_present(self, x):
        return x in self.parent
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xset, yset = self.find(x), self.find(y)
        if xset == yset:
            return
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1
        

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        dsu = UnionFind()
        for pair in similarPairs:
            dsu.add_word(pair[0])
            dsu.add_word(pair[1])
            dsu.union(pair[0], pair[1])

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            if (dsu.is_word_present(sentence1[i]) and dsu.is_word_present(sentence2[i]) and dsu.find(sentence1[i]) == dsu.find(sentence2[i])):
                continue
            return False
        return True        