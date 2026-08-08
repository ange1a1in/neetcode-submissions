class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # min-heap
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []

        for num in count.keys():
            # Push (frequency, number) into the heap
            # Python 的堆是拿元组的第一个元素来排序的,
            # 所以你想让它按什么排,就得把什么放第一位。
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


