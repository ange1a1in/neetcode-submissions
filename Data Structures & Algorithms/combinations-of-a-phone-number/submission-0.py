class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        temp = []
        # 1: []; 2: "abc"; 3: "def"
        digitToWord = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
        "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.dfs(temp, result, digits, 0, digitToWord)
        return result
    
    def dfs(self, temp, result, digits, startIndex, digitToWord):
        if len(temp) == len(digits):
            if temp:
                result.append(''.join(temp + []))
            return
        
        digit = digits[startIndex]
        for letter in digitToWord.get(digit):
            temp.append(letter)
            self.dfs(temp, result, digits, startIndex+1, digitToWord)
            temp.pop(-1)

