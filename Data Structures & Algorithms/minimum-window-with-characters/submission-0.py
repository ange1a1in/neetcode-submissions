class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # want smallest window in s that contains all characters of t
        # expand window by moving right pointer r and adding characters into a window map
        # once the window has all required characters, shrink it from the left with pointer l to make it as small as possible

        if t == "":
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # have: 已满足几种字符
        # need: 需要满足几种字符
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            # update the best result
            while have == need:
                # 当前窗口有效，记录更短的答案
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # shrink from the left
                window[s[l]] -= 1
                # 如果移走后不够了，窗口不再有效
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
