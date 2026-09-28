class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointers
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1 # advance i when we find a matching character
            j += 1 # always advance j
        
        return i == len(s)