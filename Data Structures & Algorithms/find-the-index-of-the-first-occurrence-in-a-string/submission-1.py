class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # build LPS array
        # 从字符串开头，到当前位置为止，这一段的开头和结尾，最长有多少个字符相同？
        if needle == "":
            return 0
        lps = [0] * len(needle)

        prevLPS, i = 0, 1
        # i：现在新加入的字符位置。
        # prevLPS：已经找到的相同前后缀长度，尝试在它后面再接一个字符。
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
        
        j = 0 # ptr for haystack
        i = 0 # ptr for needle

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1


