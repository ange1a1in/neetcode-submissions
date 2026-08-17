class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # prefix[j + 1] - prefix[i] = nK
        # prefix[j + 1] % k - prefix[i] % k = 0

        prefix = [0] * (len(nums) + 1)
        for i, val in enumerate(nums):
            prefix[i+1] = prefix[i] + val

        maps = {} # key: val % k; value: index

        for index, val in enumerate(prefix):
            if val % k in maps:
                right = index - 1
                left = maps[val % k]
                if right - left + 1 >= 2:
                    return True
            if val % k not in maps:
                maps[val % k] = index
        return False