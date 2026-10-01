class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.dead = TrieNode()
        self.curr_node = self.root # 当前前缀对应的节点
        self.curr_sentence = [] # 用户当前输入的全部字符

        for sentence, count in zip(sentences, times):
            self.add_to_trie(sentence, count)


    def add_to_trie(self, sentence: str, count: int):
        node = self.root

        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.sentences[sentence] += count

    def input(self, c: str) -> List[str]:
        if c == "#":
            sentence = "".join(self.curr_sentence)
            self.add_to_trie(sentence, 1)
            self.curr_sentence = []
            self.curr_node = self.root
            return []
        
        self.curr_sentence.append(c)

        if c not in self.curr_node.children:
            self.curr_node = self.dead
            return []
        
        self.curr_node = self.curr_node.children[c]

        # Python 默认从小到大排序，比较元组时，先比较第一项，第一项相同才比较第二项。
        matches = sorted(self.curr_node.sentences.items(), key = lambda x: (-x[1], x[0]))

        ans = []
        for i in range(min(3, len(matches))):
            ans.append(matches[i][0])
        return ans

        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
