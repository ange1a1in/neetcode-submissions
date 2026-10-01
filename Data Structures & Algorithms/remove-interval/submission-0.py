class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:

        # if there is no overlap, keep the interval unchanged
        # if there is overlap, need to preserve any portions that fall outside the removal range
        remove_start, remove_end = toBeRemoved

        output = []

        for start, end in intervals:
            # if there is no overlap, add the interval to the list as is
            if start > remove_end or end < remove_start:
                output.append([start, end])
            else:
                # is there a left interval we need to keep?
                if start < remove_start:
                    output.append([start, remove_start])
                
                if end > remove_end:
                    output.append([remove_end, end])
        
        return output