class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = {}
        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1
        
        maxCount = max(counts.values())

        if maxCount > (len(s) + 1) // 2:
            return ""

        max_heap = [(-freq, letter) for letter, freq in counts.items()]
        heapq.heapify(max_heap)

        res = []

        while len(max_heap) > 1:
            f1, letter1 = heapq.heappop(max_heap)
            f2, letter2 = heapq.heappop(max_heap)
            res += [letter1, letter2]
            counts[letter1] -= 1
            counts[letter2] -= 1

            if counts[letter1] > 0:
                heapq.heappush(max_heap, (-counts[letter1], letter1))
            if counts[letter2] > 0:
                heapq.heappush(max_heap, (-counts[letter2], letter2))
        
        if max_heap:
            res.append(max_heap[0][1])

        return "".join(res)










