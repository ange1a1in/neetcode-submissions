class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # min-heap
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []

        for num in count.keys():
            # Push (frequency, number) into the heap
            heapq.heappush(heap, (count[num], num))

            # If the heap size becomes greater than k, 
            # pop once to remove the smallest frequency.
            if len(heap) > k:
                heapq.heappop(heap)
        # Pop all elements from the heap and 
        # collect their numbers into the result list.
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


