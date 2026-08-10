class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = 0
        ans = 0 # end - start + 1

        prod = 1 # product

        for j in range(len(nums)):
            prod *= nums[j]
            while prod >= k and i <= j:
                prod /= nums[i]
                i += 1
            ans += (j - i + 1)
        return ans
