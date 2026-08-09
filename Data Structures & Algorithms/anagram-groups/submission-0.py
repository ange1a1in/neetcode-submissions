class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for curr in strs:
            sortedCurr = sorted(curr) # "eat" → ['a','e','t']
            s = ''.join(sortedCurr) # ['a','e','t'] → "aet",当作 key
            res[s].append(curr)


        return list(res.values())