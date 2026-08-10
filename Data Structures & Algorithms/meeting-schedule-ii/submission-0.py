"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sweep line

        # Create a map mp to record changes in the number of active meetings
        mp = defaultdict(int)
        for meeting in intervals:
            mp[meeting.start] += 1 # increment mp[start] (a meeting starts)
            mp[meeting.end] -= 1 # decrement mp[end] (a meeting ends)
        
        prev = 0 # track the number of ongoing meetings
        res = 0 # store the maximum number of simultaneous meetings
        
        # Iterate through all time points in mp in sorted order
        for time in sorted(mp.keys()):
            # update the current number of meetings
            prev += mp[time]
            res = max(res, prev)
        return res
