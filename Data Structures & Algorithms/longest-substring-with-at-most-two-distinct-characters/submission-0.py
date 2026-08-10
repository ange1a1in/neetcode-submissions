class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        count = collections.defaultdict(int)

        i = 0
        ans = 0

        for j in range(len(s)):
            count[s[j]] += 1
            while len(count) > 2: # 不同字符超过 2 种 -> 缩左边i
                count[s[i]] -= 1 # 减到 0 才真正删掉，种类数才 -1
                if count[s[i]] == 0:
                    del count[s[i]]
                i += 1 
            ans = max(ans, j-i+1)  # 窗口合法，更新最长长度
        
        return ans

