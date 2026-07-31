class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # create graph
        graph = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            graph[word] = self.get_neighbor(word, set(wordList))
        queue = collections.deque([beginWord])
        visited = set()
        visited.add(beginWord)

        # go through grph
        return self.bfs(queue, visited, graph, endWord)
    
    def get_neighbor(self, word, wordList):
        res = []
        for index, letter in enumerate(word):
            for replaceLetter in "abcdefghijklmnopqrstuvwxyz":
                if letter != replaceLetter:
                    newWord = word[:index] + replaceLetter + word[index+1:]
                    if newWord in wordList:
                        res.append(newWord)
        return res




    # level-order bfs 因为要看几步找到
    def bfs(self, queue, visited, graph, endWord):
        step = 1 
        # step: the number of words in the transformation sequence
        # beginWord 算一个单词，所以 step 初始 =1
        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                neighbors = graph.get(word,[])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        if neighbor == endWord:
                            return step + 1
                        visited.add(neighbor)
                        queue.append(neighbor)
            step += 1
        return 0




