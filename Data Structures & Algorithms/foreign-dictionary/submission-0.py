class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 看第一个不一样的字母
        # 比较长度用短的那个单词的
        graph = collections.defaultdict(list)
        degree = {}

        # 设置入度
        for word in words:
            for ch in word:
                if ch not in graph:
                    degree[ch] = 0
        
        for i in range(len(words) - 1):
            word_pre = words[i]
            word_curr = words[i+1]

            if len(word_pre) > len(word_curr) and word_pre.startswith(word_curr):
                return ''
            
            # graph from a to b; in-degree update
            m = min(len(word_pre), len(word_curr))

            for j in range(m):
                from_letter = word_pre[j]
                to_letter = word_curr[j]
                if from_letter != to_letter:
                    if to_letter not in graph[from_letter]:
                        graph[from_letter].append(to_letter)
                        degree[to_letter] += 1
                    break

            # topological sort
        queue = deque([])
        for key, val in degree.items():
            if val == 0:
                queue.append(key)
        res = []
        while len(queue) > 0:
            curr = queue.popleft()
            res.append(curr)
            for neighbor in graph[curr]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(res) != len(degree):
            return ''
            
            # 合成string
        return ''.join(res) 
    



