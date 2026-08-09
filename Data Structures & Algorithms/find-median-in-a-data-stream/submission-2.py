class MedianFinder:

    def __init__(self):
        # max-heap (small) stores the smaller half of the numbers
        # min-heap (large) stores the larger half of the numbers
        self.min_heap = [] # for larger part
        self.max_heap = [] # for smaller part
 

    def addNum(self, num: int) -> None:
        # 把 num 和 max_heap 现有的所有数放一起,取出其中最大的那个,送去 min_heap
        heapq.heappush(self.max_heap, -1 * num)
        num = -1 * heapq.heappop(self.max_heap)
        # 天然保证了 min_heap 里的每个数都 ≥ max_heap 里剩下的每个数
        heapq.heappush(self.min_heap, num)

        # rebalance: min_heap 会比 max_heap 多一个
        if len(self.min_heap) - len(self.max_heap) > 1:
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * num)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2

        
        